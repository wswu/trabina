#!/usr/bin/env python3

import glob
import os
import sys


delete = len(sys.argv) > 1 and sys.argv[1] == '-exec'
models = glob.glob('/export/b08/wwu/translit-runs/*/opennmt/models/*')
for m in models:
    if 'epoch25' not in m:
        print(m)
        if delete:
            os.remove(m)
if not delete:
    print('Run with -exec to delete')
