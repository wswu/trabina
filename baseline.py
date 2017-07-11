#!/usr/bin/env python3

import sys
from unidecode import unidecode

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        for line in fin:
            print(unidecode(line.strip()))
