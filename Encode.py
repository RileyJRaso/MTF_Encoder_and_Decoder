#!/usr/bin/env python3

import sys
import Encode_And_Decode

if len(sys.argv) < 2:
    print("usage: ./encode.py <filename>")
    sys.exit(1)

Encode_And_Decode.encode(sys.argv[1])
