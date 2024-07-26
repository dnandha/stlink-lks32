# stlink-brightway

## Installation

## Change scooter SN

### Download files
1. Download [Pack](Linko.LKS08x.1.1.4.pack) ([Source](https://www.lksmcu.com/static/upload/file/20230113/Linko.LKS08x_v1.14.zip))
1. Download [SN script](replace_sn.py)

### Dump flash
`python -m pyocd cmd -c savemem 0 0x10000 mcu_fw.bin --pack Linko.LKS08x.1.1.4.pack --target lks32mc081c8t8`

## Change SN
2. Run `python replace_sn.py mcu_fw_mod.bin <SERIAL_NUMBER>`
For `<SERIAL_NUMBER>` check [Serial Number Prefixes](#serial-number-prefixes)

### Write modded bin back to flash
`python -m pyocd load mcu_fw_mod.bin --pack Linko.LKS08x.1.1.4.pack --target lks32mc081c8t8`

## Serial Number Prefixes (Global)
| Model | SN |
| --- | --- |
| 3 Lite | 35793 |
| 4 | 46441 |
| 4 Lite | 46415 |
| 4 Ultra | 37829 |
| 4 Pro (2nd) | 53931 |
