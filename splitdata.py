#!/usr/bin/env python3

import random
import sys


random.seed(12345)


def pp(s):
    return s.strip().replace(' ', '_').replace('', ' ').strip()


def splitdata(datadir, src, tgt, outdir):
    with open(f'{datadir}/{src}') as srcfile:
        src_words = srcfile.read().splitlines()
    with open(f'{datadir}/{tgt}') as tgtfile:
        tgt_words = tgtfile.read().splitlines()
    pairs = list(zip(src_words, tgt_words))
    pairs = [(s, t) for s, t in pairs if s != '-' and t != '-']
    random.shuffle(pairs)

    train = pairs[:int(len(pairs) * 0.6)]
    dev = pairs[int(len(pairs) * 0.6):int(len(pairs) * 0.8)]
    test = pairs[int(len(pairs) * 0.8):]

    for name, datasplit in [('train', train), ('dev', dev), ('test', test)]:
        with open(f'{outdir}/{name}.{src}', 'w') as srcfile, \
                open(f'{outdir}/{name}.{tgt}', 'w') as tgtfile:
            for s, t in datasplit:
                print(pp(s), file=srcfile)
                print(pp(t), file=tgtfile)


if __name__ == '__main__':
    splitdata(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
