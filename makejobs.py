#!/usr/bin/env python3

import os
import textwrap


os.makedirs('qsubs', exist_ok=True)
os.makedirs('out', exist_ok=True)
os.makedirs('err', exist_ok=True)

counter = 0
for lang in os.listdir('data/by-lang'):
    counter += 1
    with open('qsubs/translit.' + str(counter), 'w') as f:
        print('SRC=' + lang, file=f)
        print('source ./run-compare.sh', file=f)

with open('translit.sh', 'w') as f:
    print(textwrap.dedent(f'''\
        #$ -cwd
        #$ -t 1-{counter}
        #$ -o out
        #$ -e err
        sh qsubs/translit.$SGE_TASK_ID'''), file=f)
