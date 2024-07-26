# ST-Link LKS3209x
This repo describes how to dump and flash LKS3208x chips with the help of a ST-Link probe.

## Installation
Install python and pyocd with pip: `pip install pyocd`

### Required files
1. Download [Pack](Linko.LKS08x.1.1.4.pack) ([Source](https://www.lksmcu.com/static/upload/file/20230113/Linko.LKS08x_v1.14.zip))
1. Download [SN script](replace_sn.py)

## Basic procedure

### Hookup ST-Link
Like this:

![image](swd_pinout.png)

### Dump flash
Using `pyocd` and the Pack file downloaded before:

`python -m pyocd cmd -c savemem 0 0x10000 mcu_fw.bin --pack Linko.LKS08x.1.1.4.pack --target lks32mc081c8t8`

### Modify bin
Copy `mcu_fw.bin` to `mcu_fw_mod.bin` and make changes. See [Change SN](#change-sn) for an example.

### Write bin back to flash
Using `pyocd` and the Pack file downloaded before:

`python -m pyocd load mcu_fw_mod.bin --pack Linko.LKS08x.1.1.4.pack --target lks32mc081c8t8`

#### Restore original binary
Simply run the above command with `mcu_fw.bin` instead of `mcu_fw_mod.bin`.

Advise: Keep the original binary in a safe place!


## Example: Change SN
Using the SN script downloaded before:

`python replace_sn.py mcu_fw_mod.bin <SERIAL_NUMBER>`

For `<SERIAL_NUMBER>` check [Serial Number Prefixes](#serial-number-prefixes)

## Serial Number Prefixes (Global)
| Model | SN |
| --- | --- |
| 3 Lite | 35793 |
| 4 | 46441 |
| 4 Lite | 46415 |
| 4 Ultra | 37829 |
