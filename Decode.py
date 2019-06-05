#!/usr/bin/env python3

import sys
import Encode_And_Decode

if len(sys.argv) < 2:
    print("usage: ./decode.py <filename>")
    sys.exit(1)

Encode_And_Decode.decode(sys.argv[1])
