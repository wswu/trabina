#!/usr/bin/env python3

import os
import subprocess
import sys

exec_flag = len(sys.argv) >= 2 and sys.argv[1] == '-exec'
output_files = [
    '/moses/test.nlist',
    '/moses-with-pre/test.nlist',
    '/moses-with-post/test.nlist',
    '/unidecode/test.nlist',
    '/opennmt/test.nlist']

errors = []
rootdir = '/export/b08/wwu/translit-runs'
for expdir in os.listdir(rootdir):
    for out in output_files:
        path = os.path.join(rootdir, expdir, out)
        if not os.path.isfile(path) or os.stat(path).st_size == 0:
            print(expdir + path)
            errors.append(expdir[:-4])  # remove -eng

langs = os.listdir('data/by-lang')
langs = {e: i + 1 for i, e in enumerate(langs)}

errors = sorted(set(errors))
for e in errors:
    command = 'qsub -cwd -o out/ -e err/ qsubs/translit.' + str(langs[e])
    print(command)
    if exec_flag:
        subprocess.run(command, shell=True)

print(str(len(errors)) + ' need rerunning')
print(','.join([str(langs[e]) for e in errors]))
