
SEQUITUR="/home/wwu/softw/anaconda3/envs/py27/bin/python /home/wwu/softw/sequitur-g2p/g2p.py"

python make-sequitur-bitext.py $DATADIR/train.$SRC $DATADIR/train.$TGT > $DATADIR/train.seq
python make-sequitur-bitext.py $DATADIR/dev.$SRC $DATADIR/dev.$TGT > $DATADIR/dev.seq
sed 's/ //g' $DATADIR/test.$SRC > $DATADIR/test.seq

$SEQUITUR --train $DATADIR/train.seq --devel $DATADIR/dev.seq --write-model $EXPDIR/model-1
$SEQUITUR --train $DATADIR/train.seq --devel $DATADIR/dev.seq --ramp-up --model $EXPDIR/model-1 --write-model $EXPDIR/model-2
$SEQUITUR --train $DATADIR/train.seq --devel $DATADIR/dev.seq --ramp-up --model $EXPDIR/model-2 --write-model $EXPDIR/model-3
$SEQUITUR --train $DATADIR/train.seq --devel $DATADIR/dev.seq --ramp-up --model $EXPDIR/model-3 --write-model $EXPDIR/model-4

$SEQUITUR --apply $DATADIR/test.seq --model $EXPDIR/model-4 --encoding=UTF-8 > $EXPDIR/test.seqout 2> $EXPDIR/test.err

python seqout2nlist.py $DATADIR/test.seq $EXPDIR/test.seqout > $EXPDIR/test.nlist
