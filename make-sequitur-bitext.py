#!/usr/bin/env python3

'''
Make sequitur bitext from aligned, character-split src and tgt bitext files.

Output format is source\tt a r g e t
'''

import sys

with open(sys.argv[1]) as fsrc, open(sys.argv[2]) as ftgt:
    for src, tgt in zip(fsrc, ftgt):
        src = src.strip().replace(' ', '')
        tgt = tgt.strip()
        print(src + '\t' + tgt)
