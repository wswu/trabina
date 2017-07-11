#!/usr/bin/env python3

'''
Convert sequitur output (might be missing entries) to an aligned 1-best list
'''

import sys

testsrc = sys.argv[1]
testout = sys.argv[2]

test_src = []
with open(testsrc) as fin:
    for line in fin:
        word = line.strip()
        test_src.append(word)

test_out = {}
with open(testout) as fin:
    for line in fin:
        src, tgt = line.strip('\n').split('\t')
        test_out[src] = tgt

for src in test_src:
    print(test_out.get(src, ''))
