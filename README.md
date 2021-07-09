# patch2h
![GitHub](https://img.shields.io/github/license/R0rt1z2/patch2h)

Convert MediaTek Bluetooth patch files into standard C/C++ headers.

## Requirements
This binary requires Python 3 or newer installed on your system. 
It currently supports Windows, Linux and MacOS architectures.

## Usage
```
patch2h.py input_file output_file
```
- `<input_file>` = input_file, mt7662_patch_e3_hdr.bin (example)
- `<output_file>` = input_file, mt7662_patch_e3_hdr.h (example)

## Example
This is a simple example on a Linux system: 
```
r0rt1z2@r0rt1z2$ python3 patch2h.py mt7662_patch_e3_hdr.bin mt7662_patch_e3_hdr.h
[?] Patch build date = 2013-12-10
[?] Patch model = ALPS
[*] Dumping data from mt7662_patch_e3_hdr.bin to 'mt7662_patch_e3_hdr.h'...
[+] All done, check 'mt7662_patch_e3_hdr.h'!
r0rt1z2@r0rt1z2$
```

## License
* This program is licensed under the GNU General Public License (v3). See `LICENSE` for details.