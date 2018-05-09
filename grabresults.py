#!/usr/bin/env python3

import glob
import re

for f in sorted(glob.glob('/export/b08/wwu/translit-runs/*/results2')):
    with open(f) as fin:
        scores = [str(round(float(line.split('\t')[1]), 4))
                  for line in fin.read().strip().split('\n')]
        print(re.match('.*\/(.*)\/results', f).group(1) + ',' + ','.join(scores))
