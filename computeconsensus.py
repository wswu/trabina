#!/usr/bin/env python3

import os
import sys
from collections import Counter


main_folder = '/export/b08/wwu/translit-runs'
systems = ['unidecode', 'sequitur', 'moses', 'moses-with-pre', 'moses-with-post', 'opennmt2']

avg_perf = [0.141259291, 0.21051402, 0.209043243, 0.210633615, 0.171329223, 0.098129561]
avg_perf_counts = [int(x * 100) for x in avg_perf]

def flatten(l):
    return [x for sl in l for x in sl]

def consensus():
    for expdir in os.listdir(main_folder):
        if not os.path.isdir(main_folder + '/' + expdir):
            continue

        os.makedirs(f'{main_folder}/{expdir}/consensus', exist_ok=True)
        files = [open(f'{main_folder}/{expdir}/{s}/test.nlist') for s in systems]
        with open(f'{main_folder}/{expdir}/consensus/test.nlist', 'w') as fout:
            for words in zip(*files):
                words = [w.strip() for w in words]
                counter = Counter(words)
                consensus = counter.most_common()[0][0]
                print(consensus, file=fout)
        for f in files:
            f.close()

        files = [open(f'{main_folder}/{expdir}/{s}/test.nlist') for s in systems]
        os.makedirs(f'{main_folder}/{expdir}/weighted', exist_ok=True)
        with open(f'{main_folder}/{expdir}/weighted/test.nlist', 'w') as fout:
            for words in zip(*files):
                words = [w.strip() for w in words]
                words = flatten([word] * count for word, count in zip(words, avg_perf_counts))
                counter = Counter(words)

                consensus = counter.most_common()[0][0]
                print(consensus, file=fout)

def output():
    systems.append('consensus')
    systems.append('weighted')

    for expdir in os.listdir(main_folder):
        files = [open(f'{main_folder}/{expdir}/{s}/test.nlist') for s in systems]
        with open(f'trabina-output/{expdir}.txt', 'w') as fout:
            print('\t'.join(systems), file=fout)
            for words in zip(*files):
                words = [w.strip() for w in words]
                print('\t'.join(words), file=fout)


if __name__ == '__main__':
    output()
