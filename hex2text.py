#!/usr/bin/python
from __future__ import with_statement
import sys
import binascii

READ_BLOCKSIZE = 16

def main(argv):
    argc = len(argv)
    if argc < 3:
        print 'Usage:', argv[0], 'dumpdata.bin output.txt'
        sys.exit(1)

    with file(argv[1], "rb") as file_inp, file(argv[2], "w") as file_out:
        while True:
            byte_s = file_inp.read(READ_BLOCKSIZE)
            if not byte_s:
                break
            hex_char_repr = binascii.hexlify(byte_s)
            file_out.write(hex_char_repr)
            file_out.write("\n")

if __name__ == '__main__':
    main(sys.argv)