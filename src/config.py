import os

PROJECT_NAME='weixin_12_25'
data_index='0'


MODEL_NAME='CNN'
#MODEL_NAME='GRU'
#MODEL_NAME='LSTM'

TRAIN_DATA_PATH = '../data/'+PROJECT_NAME+'/train/'
VALIDATION_DATA_PATH = '../data/'+PROJECT_NAME+'/test/'
TEST_DATA_PATH = '../data/'+PROJECT_NAME+'/test/'



TRAIN_DATA_NAME= 'data.'+data_index
TRAIN_LABEL_NAME= 'label.'+data_index

VALIDATION_DATA_NAME= 'data.'+data_index
VALIDATION_LABEL= 'label.'+data_index

TEST_DATA_NAME= 'data.'+data_index
TEST_LABEL_NAME= 'label.'+data_index

INFERENCE_RESULT_NAME='result.'+data_index


CPT_PATH = '../checkpoints/'+PROJECT_NAME+'/'+MODEL_NAME+'/'+TRAIN_DATA_NAME
LOG_PATH='../log/'+PROJECT_NAME+'/'+MODEL_NAME+'/'+TRAIN_DATA_NAME
VISUALIZATION_PATH ='../visualization/'+PROJECT_NAME+'/'+MODEL_NAME+'/'+TRAIN_DATA_NAME

UNK_ID = 0
PAD_ID = 1
START_ID = 2
EOS_ID = 3

NUM_STEPS=20
NUM_LAYERS = 2
HIDDEN_SIZE = [128,256]
BATCH_SIZE = 128
LR = 0.0003
#NUM_SAMPLES = 512
NUM_CLASSES=24
EMBEDDING_SIZE=256
KERNEL_SIZE=[2,3,4]
NUM_FILTERS=64
DROPOUT_KEEP_PROB=0.3

READ_IN_FORMAT=[[0]]*(NUM_STEPS)
ONE_HOT_TAG=False
EPOCH_NUM = 1000


PRETRAIN_EMBD_TAG=False
PRETRAIN_EMBD_TRAINABLE=False
'''
PRETRAIN_EMBD_SIZE=50
PRETRAIN_EMBD_VOCAB_SIZE = 400002
PRETRAIN_EMBD_PATH ='../data/glove.6B.50d.txt'
'''

MODEL_BI_DIRECTION = True
#INITIALIZER='xavier'
INITIALIZER = None

ATTENTION_TAG=False
SELF_ATTENTION_TAG = False
ATTENTION_SIZE = 15
NUM_TOPICS =1
ATTENTION_COEF=0.004
VISUALIZATION = False

CKPT_FILE_NAME='/-260000'
TF_PARAMETER_NPY_PATH ='../model/'+PROJECT_NAME+'/'+MODEL_NAME+'/'+TRAIN_DATA_NAME+'/tf/'+CKPT_FILE_NAME+'/'

if os.path.exists('../data/'+PROJECT_NAME+'/vocab.txt'):
    VOCAB_SIZE=sum(1 for line in open('../data/'+PROJECT_NAME+'/vocab.txt','r',encoding='utf-8'))
#VOCAB_SIZE=2776
