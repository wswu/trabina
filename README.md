# trabina

Transliteration using bible names. Requires Python 3.6 and [Unidecode](https://pypi.python.org/pypi/Unidecode) for computing a baseline.

Set the relevant paths in `train-{system}.sh` and run with

    python makejobs.py
    qsub translit.sh

For failed runs, resubmit with

    python checkfailed.py -exec
