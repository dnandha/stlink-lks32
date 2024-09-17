def replace_string_in_binary(file_path, new_value, offset=0xfc48):
    # Convert the new value to bytes
    new_value_bytes = bytearray()
    separator = b'\x00\x00\x00'
    for byte in new_value.encode('utf-8'):
        new_value_bytes.extend([byte])  # Add the original byte
        new_value_bytes.extend(separator)  # Add 00 00 00

    # Open the file in read-write binary mode
    with open(file_path, 'r+b') as file:
        # Move the cursor to the specified offset
        file.seek(offset)

        # Write the new bytes to the file
        file.write(new_value_bytes)


if __name__ == "__main__":
    import sys

    # Example usage
    binary_file_path = sys.argv[1]
    new_string_value = sys.argv[2]

    replace_string_in_binary(binary_file_path, new_string_value)
