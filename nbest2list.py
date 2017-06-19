#!/usr/bin/env python3

from itertools import groupby
import sys

def readnbestlist(filename):
  data = []
  with open(filename) as fin:
    for line in fin:
      index, word, features, score = line.split('|||')
      data.append((index, word.strip().replace(' ', '').replace('_', ' '), score.strip()))
  grouped = []
  for key, items in groupby(data, key=lambda x: x[0]):
    items = list(items)
    grouped.append([word + '(' + score + ')' for index, word, score in items])
  return grouped


def main():
  for hyps in readnbestlist(sys.argv[1]):
    print(','.join(hyps))


if __name__ == '__main__':
  main()
