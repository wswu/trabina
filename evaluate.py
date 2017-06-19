#!/usr/bin/env python3

import sys


def compute_accuracy(goldpath, hypspath):
    with open(goldpath) as goldfile, open(hypspath) as hypsfile:
        correct = 0
        total = 0
        for gold, hyp in zip(goldfile, hypsfile):
            gold = gold.strip().replace(' ', '').replace('_', ' ')
            hyp = hyp.strip().replace(' ', '').replace('_', ' ')

            # for n-best list
            if ',' in hyp:
                hyp = hyp.split(',')[0]
                hyp = hyp[:hyp.find('(')]

            if gold == hyp:
                correct += 1
            total += 1
        return correct / total if total > 0 else 0.0


if __name__ == '__main__':
    expdir = sys.argv[1]
    tgtlang = sys.argv[2]
    print('Moses')
    print(compute_accuracy(f'{expdir}/test.{tgtlang}', f'{expdir}/test.nlist'))
    print('Unidecode')
    print(compute_accuracy(f'{expdir}/test.{tgtlang}', f'{expdir}/test.unidecode'))
