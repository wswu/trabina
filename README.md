# trabina

Transliteration of Bible names. Requires Python 3.6 and [Unidecode](https://pypi.python.org/pypi/Unidecode) for computing a baseline.

Set the relevant paths in `train-{system}.sh` and run with

    python makejobs.py
    qsub translit.sh

For failed runs, resubmit with

    python checkfailed.py -exec

Bible names translation matrix in `data`. Transliteration output in `trabina-output`.

Citations

- *Creating a Translation Matrix of the Bible's Names Across 591 Languages.* Winston Wu, Nidhi Vyas, and David Yarowsky (2018).
- *A Comparative Study of Extremely Low-Resource Transliteration of the World's Languages.* Winston Wu and David Yarowsky (2018).
