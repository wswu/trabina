#!/usr/bin/env python3

import sys
from unidecode import unidecode

with open(sys.argv[1], encoding='utf-8') as fin:
    for line in fin:
        # remove spaces first b/c one char can become multiple chars
        print(unidecode(' '.join(line.strip().replace(' ', ''))))
