NAMESDIR=$(pwd)/data/by-lang/
MOSES=/home/wwu/mosesdecoder

PYTHON=/home/wwu/softw/anaconda3/envs/py36/bin/python

#SRC=aak_aak
TGT=eng
ROOTDIR=/export/b08/wwu/translit-runs/$SRC-$TGT
DATADIR=$ROOTDIR/data

mkdir -p $ROOTDIR
mkdir -p $DATADIR

$PYTHON splitdata.py $NAMESDIR $SRC $TGT $DATADIR

# baseline
mkdir -p $ROOTDIR/unidecode
$PYTHON baseline.py $DATADIR/test.$SRC > $ROOTDIR/unidecode/test.nlist

# sequitur
mkdir -p $ROOTDIR/sequitur
EXPDIR=$ROOTDIR/sequitur
source ./train-sequitur.sh

# vanilla
mkdir -p $ROOTDIR/moses
EXPDIR=$ROOTDIR/moses
source ./train-moses.sh
$PYTHON nbest2list.py $EXPDIR/test.nbest > $EXPDIR/test.nlist

# post process the output of above
mkdir -p $ROOTDIR/moses-with-post
EXPDIR=$ROOTDIR/moses-with-post
cp $ROOTDIR/moses/test.nlist $EXPDIR/test.nlist.orig
$PYTHON baseline.py $EXPDIR/test.nlist.orig > $EXPDIR/test.nlist

# neural
mkdir -p $ROOTDIR/opennmt
EXPDIR=$ROOTDIR/opennmt
source ./train-nmt.sh

# with preprocessing (do this last, since we change SRC)
mkdir -p $ROOTDIR/moses-with-pre
EXPDIR=$ROOTDIR/moses-with-pre
$PYTHON pretransliterate.py $DATADIR/train.$SRC > $DATADIR/train.$SRC-pre
$PYTHON pretransliterate.py $DATADIR/dev.$SRC > $DATADIR/dev.$SRC-pre
$PYTHON pretransliterate.py $DATADIR/test.$SRC > $DATADIR/test.$SRC-pre
SRC=$SRC-pre
source ./train-moses.sh
$PYTHON nbest2list.py $EXPDIR/test.nbest > $EXPDIR/test.nlist

$PYTHON evaluate.py $DATADIR/test.$TGT $ROOTDIR/unidecode $ROOTDIR/moses $ROOTDIR/moses-with-pre $ROOTDIR/moses-with-post $ROOTDIR/sequitur $ROOTDIR/opennmt > $ROOTDIR/results
