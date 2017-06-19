MOSES=/home/wwu/mosesdecoder

SRC=rus_centralasian
TGT=eng

DATA=$(pwd)/data/by-lang/
EXPDIR=/export/b08/wwu/$SRC-$TGT

mkdir -p $EXPDIR

# Preprocess
python splitdata.py $DATA $SRC $TGT $EXPDIR

# Run baseline
python baseline.py $EXPDIR/test.$SRC > $EXPDIR/test.unidecode

# Make LM
$MOSES/bin/lmplz -o 4 -S 1G --discount_fallback < $EXPDIR/train.$TGT > $EXPDIR/lm.arpa
$MOSES/bin/build_binary $EXPDIR/lm.arpa $EXPDIR/lm.blm

# Train
$MOSES/scripts/training/train-model.perl -mgiza -root-dir $EXPDIR -corpus $EXPDIR/train -f $SRC -e $TGT -lm 0:4:$EXPDIR/lm.blm -external-bin-dir $MOSES/tools -distortion-limit 0

# Tune
pushd $EXPDIR
$MOSES/scripts/training/mert-moses.pl $EXPDIR/dev.$SRC $EXPDIR/dev.$TGT $MOSES/bin/moses $EXPDIR/model/moses.ini --mertdir $MOSES/bin &> $EXPDIR/mert.out

# Decode
$MOSES/bin/moses -f $EXPDIR/mert-work/moses.ini -n-best-list $EXPDIR/test.nbest 10 distinct --distortion-limit 0 < $EXPDIR/test.$SRC

popd

# Evaluate
python nbest2list.py $EXPDIR/test.nbest > $EXPDIR/test.nlist
python evaluate.py $EXPDIR $TGT > $EXPDIR/results
