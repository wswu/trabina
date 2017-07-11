#!/usr/bin/env python3

'''
Convert Moses nbest list to simple list
'''

from itertools import groupby
import sys


def readnbestlist(filename):
    data = []
    with open(filename) as fin:
        for line in fin:
            index, word, features, score = line.split('|||')
            data.append((index, word.strip(), score.strip()))
    grouped = []
    for key, items in groupby(data, key=lambda x: x[0]):
        items = list(items)
        # grouped.append([word + '(' + score + ')' for index, word, score in items])
        grouped.append([items[0][1]])  # for now, just use 1-best
    return grouped


def main():
    for hyps in readnbestlist(sys.argv[1]):
        print(','.join(hyps))


if __name__ == '__main__':
    main()
