#DATA=$(pwd)/data/by-lang/
MOSES=/home/wwu/mosesdecoder

#SRC=rus_centralasian
#TGT=eng
#EXPDIR=/export/b08/wwu/$SRC-$TGT


# Make LM
$MOSES/bin/lmplz -o 4 -S 1G --discount_fallback < $DATADIR/train.$TGT > $EXPDIR/lm.arpa
$MOSES/bin/build_binary $EXPDIR/lm.arpa $EXPDIR/lm.blm

# Train
$MOSES/scripts/training/train-model.perl -mgiza -root-dir $EXPDIR -corpus $DATADIR/train -f $SRC -e $TGT -lm 0:4:$EXPDIR/lm.blm -external-bin-dir $MOSES/tools -distortion-limit 0

# Tune
pushd $EXPDIR
$MOSES/scripts/training/mert-moses.pl $DATADIR/dev.$SRC $DATADIR/dev.$TGT $MOSES/bin/moses $EXPDIR/model/moses.ini --mertdir $MOSES/bin &> $EXPDIR/mert.out

# Decode
$MOSES/bin/moses -f $EXPDIR/mert-work/moses.ini -n-best-list $EXPDIR/test.nbest 10 distinct --distortion-limit 0 < $DATADIR/test.$SRC

popd
