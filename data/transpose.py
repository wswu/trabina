#!/usr/bin/env python3

import os
import sys


def transpose(indir, outdir):
    data = []
    langs = []
    langs_filled = False

    for f in sorted(os.listdir(indir)):
        names = []
        with open(indir + '/' + f) as fin:
            for line in fin:
                lang, name = line.strip('\n').split('\t')
                names.append(name)
                if not langs_filled:
                    langs.append(lang)
        langs_filled = True
        data.append(names)

    data = list(zip(*data))
    for lang, names in zip(langs, data):
        with open(outdir + '/' + lang, 'w') as fout:
            for name in names:
                print(name, file=fout)


if __name__ == '__main__':
    transpose(sys.argv[1], sys.argv[2])
