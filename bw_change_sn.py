import os
import re

# Flash size → base of the packed serial page (ASCII + 3×00 per char).
SERIAL_PAGE = {
    0x10000: 0xFC00,
    0x20000: 0x1F800,
}

# Legacy absolute offsets (page + 0x48) used when the ID field cannot be found.
LEGACY_OFFSET = {
    0x10000: 0xFC48,
    0x20000: 0x1F848,
}

PAGE_CHARS = 64  # scan window in packed characters


def _unpack_page(data: bytes, page_base: int, nchars: int = PAGE_CHARS) -> str:
    chars = []
    for i in range(nchars):
        off = page_base + i * 4
        if off + 4 > len(data):
            break
        b = data[off : off + 4]
        if b[1:] == b"\x00\x00\x00" and 32 <= b[0] < 127:
            chars.append(chr(b[0]))
        else:
            chars.append("\0")
    return "".join(chars)


def find_sn_offset(data: bytes, file_size: int) -> int:
    """Return file offset of the packed `NNNNN/…` Series No. field."""
    page_base = SERIAL_PAGE[file_size]
    text = _unpack_page(data, page_base)
    m = re.search(r"\d{5}/", text)
    if m:
        return page_base + m.start() * 4
    return LEGACY_OFFSET[file_size]


def pack_sn(value: str) -> bytes:
    out = bytearray()
    for byte in value.encode("utf-8"):
        out.append(byte)
        out.extend(b"\x00\x00\x00")
    return bytes(out)


def replace_string_in_binary(file_path, new_value):
    file_size = os.path.getsize(file_path)

    if file_size not in SERIAL_PAGE:
        raise ValueError("File size is not 0x10000 or 0x20000, aborting")

    with open(file_path, "r+b") as file:
        data = file.read()
        offset = find_sn_offset(data, file_size)
        packed = pack_sn(new_value)
        if offset + len(packed) > file_size:
            raise ValueError("SN too long for serial page")
        file.seek(offset)
        file.write(packed)


if __name__ == "__main__":
    import sys

    binary_file_path = sys.argv[1]
    new_string_value = sys.argv[2]

    replace_string_in_binary(binary_file_path, new_string_value)
