#!/usr/bin/env python3

import os.path
import sys

import editdistance


def compute_accuracy(goldpath, hypspath):
    with open(goldpath, encoding='utf-8') as goldfile, \
         open(hypspath, encoding='utf-8') as hypsfile:
        correct = 0
        total = 0
        for gold, hyp in zip(goldfile, hypsfile):
            gold = gold.strip().replace(' ', '').replace('_', ' ')
            hyp = hyp.strip().replace(' ', '').replace('_', ' ')

            # for n-best list
            if '(' in hyp:
                hyp = hyp.split(',')[0]
                hyp = hyp[:hyp.find('(')]

            if gold == hyp:
                correct += 1
            total += 1
        return correct / total if total > 0 else 0.0


def compute_avg_distance(goldpath, hypspath):
    with open(goldpath, encoding='utf-8') as goldfile, \
         open(hypspath, encoding='utf-8') as hypsfile:
        dist = 0
        total = 0
        for gold, hyp in zip(goldfile, hypsfile):
            gold = gold.strip().replace(' ', '').replace('_', ' ')
            hyp = hyp.strip().replace(' ', '').replace('_', ' ')

            # for n-best list
            if '(' in hyp:
                hyp = hyp.split(',')[0]
                hyp = hyp[:hyp.find('(')]

            dist += editdistance.eval(gold, hyp)
            total += len(gold)
        return dist / total if total > 0 else 0.0


if __name__ == '__main__':
    goldpath = sys.argv[1]
    for nbestfile in sys.argv[2:]:
        model = os.path.basename(nbestfile)
        acc = compute_accuracy(goldpath, nbestfile + '/test.nlist')
        print(model + '\t' + str(acc))
