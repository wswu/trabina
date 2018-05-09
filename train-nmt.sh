# SRC=aak_aak
TGT=eng
DATADIR=/export/b08/wwu/translit-runs/$SRC-eng/data
EXPDIR=/export/b08/wwu/translit-runs/$SRC-eng/opennmt2
OPENNMT=/home/wwu/softw/OpenNMT

export OMP_NUM_THREADS=2
source /home/wwu/torch/install/bin/torch-activate

# rm -r $EXPDIR
mkdir -p $EXPDIR

pushd $OPENNMT
# th preprocess.lua \
#     -train_src $DATADIR/train.$SRC \
#     -train_tgt $DATADIR/train.$TGT \
#     -valid_src $DATADIR/dev.$SRC \
#     -valid_tgt $DATADIR/dev.$TGT \
#     -save_data $EXPDIR/data

# mkdir -p $EXPDIR/models/

#old_model = `ls $EXPDIR/models/ | grep epoch25`

# th train.lua \
#     -data $EXPDIR/data-train.t7 \
#     -save_model $EXPDIR/models/model \
#     -rnn_size 200 \
#     -word_vec_size 200 \
#     -rnn_type GRU \
#     -optim adadelta \
#     -dropout 0.2 \
#     -end_epoch 50 \
#     -save_every_epochs 5 | tee $EXPDIR/output.log
#     # -train_from $modelname \
#     # -continue true | tee $EXPDIR/output.log

#modelname=`ls $EXPDIR/models/ | grep epoch50`

modelname=`~/trabina/lowestperp.py $EXPDIR/models`
echo $modelname > $EXPDIR/bestmodel

th translate.lua \
    -model $EXPDIR/models/$modelname \
    -src $DATADIR/test.$SRC \
    -output $EXPDIR/test.nlist

popd
