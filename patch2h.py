#!/usr/bin/env python3

         #====================================================#
         #              FILE: patch2h.py                      #
         #              AUTHOR: R0rt1z2                       #
         #              DATE: 2021                            #
         #====================================================#

#   MediaTek Bluetooth patch files converter:
#   "python3 patch2h.py input_file output_file.
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import struct
import io

def str_read(file, a):
    return str(file.read(a).decode("utf-8").strip())

def write_headers(in_file, out_file, rom_name):
    out_file.seek(0)
    out_file.write('''/* \n* AUTO GENERATED CODE, DO NOT MODIFY IT \n*/''')

    in_file.seek(0)
    out_file.write('\n\n#define BUILD_DATE "{}"\n'.format(str_read(in_file, 4) + "-" + str_read(in_file, 2) + "-" + str_read(in_file, 2)))

    in_file.seek(16)
    offset = 16 + (in_file.read().find(b'\x8a\x10') - 16)
    in_file.seek(16)
    out_file.write('#define MODEL "{}"\n\n'.format(str_read(in_file, offset)))
    
    in_file.seek(0)
    out_file.write("unsigned char {}[]".format(rom_name))

def write_data(in_file, out_file):
    i = 0
    out_file.seek(0, io.SEEK_END)
    in_file.seek(0)
    
    out_file.write(" = {\n")
    
    while True:
        try:
            data = in_file.read(1)
            hex_data = "0x%s" % data.hex()
        except:
            print("[!] Found invalid data!")
            pass
        
        if not data:
            break # EOF
        
        if i >= 16:
            out_file.write("\n")
            i = 0
            
        out_file.write("{}, ".format(hex_data))
        i += 1
    
    out_file.write("};\n")

def main():
    if len(sys.argv) > 2:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        rom_name = sys.argv[2]
    else:
        print("[-] Missing arguments")
        sys.exit(1)

    if ".h" not in output_file:
        output_file = "{}.h".format(output_file)
    elif ".h" in output_file:
        rom_name = sys.argv[2].replace(".h", "")

    try:
        in_fp = open(input_file, "rb")
    except Exception as e:
        print("[-] Couldn't open '{}' :(".format(input_file))

    try:
        out_fp = open(output_file, "w")
    except Exception as e:
        print("[-] Couldn't open '{}' :(".format(output_file))

    print("[*] Writing headers...")
    write_headers(in_fp, out_fp, rom_name)
    
    print("[*] Dumping data from {} to '{}'...".format(input_file, output_file))
    write_data(in_fp, out_fp)
    
    print("[+] All done, check '{}'!".format(output_file))

if __name__ == "__main__":
    main()