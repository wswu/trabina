SRC=$1
TGT=eng
DATADIR=/export/b08/wwu/translit-runs/$SRC-eng/data
EXPDIR=/export/b08/wwu/translit-runs/$SRC-eng/opennmt
OPENNMT=/home/wwu/softw/OpenNMT

export OMP_NUM_THREADS=1
source /home/wwu/torch/install/bin/torch-activate

rm -r $EXPDIR
mkdir -p $EXPDIR

pushd $OPENNMT
th preprocess.lua \
    -train_src $DATADIR/train.$SRC \
    -train_tgt $DATADIR/train.$TGT \
    -valid_src $DATADIR/dev.$SRC \
    -valid_tgt $DATADIR/dev.$TGT \
    -save_data $EXPDIR/data

mkdir -p $EXPDIR/models/

th train.lua \
    -data $EXPDIR/data-train.t7 \
    -save_model $EXPDIR/models/model \
    -rnn_size 200 \
    -optim adadelta \
    -end_epoch 25

modelname=`ls $EXPDIR/models/ | grep epoch25`

th translate.lua \
    -model $EXPDIR/models/$modelname \
    -src $DATADIR/test.$SRC \
    -output $EXPDIR/test.nlist

popd
