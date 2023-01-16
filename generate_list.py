# author : Baijun Feng
'''
Generate train.list and test.list for model training, no directoy for 'scene'
Use after convert_mat_to_txt.py
Be sure that the the only difference between a image file and its corresponding txt label file is the postfix name. 
'''

# load libraries
import scipy.io as sio
import numpy as np
import os

data_dir = "./dataset/data/"
train_filelist = os.listdir(data_dir + "train/")
test_filelist = os.listdir(data_dir + "test/")

train_list = []
name_set = set()

for train_file in train_filelist:
    if "GT" in train_file:
        continue
    name = train_file[:len(train_file)-4]
    if name not in name_set:
        new_list = list(["train/" + name + ".jpg", "train/GT_" + name + ".txt"])
        train_list.append(new_list)
        

np.savetxt(data_dir + "train.list", train_list, "%s")
print("write train.list!")

test_list = []
name_set.clear()

for test_file in test_filelist:
    if "GT" in test_file:
        continue
    name = test_file[:len(test_file)-4]
    if name not in name_set:
        new_list = list(["test/" + name + ".jpg", "test/GT_" + name + ".txt"])
        test_list.append(new_list)


np.savetxt(data_dir + "test.list", test_list, "%s")
print("write test.list!")
print("finishes!")



'''
python train.py --data_root ./dataset/data/ --dataset_file SHHA  --epochs 3500  --lr_drop 3500  --output_dir ./logs  --checkpoints_dir ./weights  --tensorboard_dir ./logs  --lr 0.0001  --lr_backbone 0.00001  --batch_size 8  --eval_freq 1  --gpu_id 0

python train.py --data_root ./dataset/data/ --dataset_file SHHA  --epochs 3500  --lr_drop 3500  --output_dir ./logs  --checkpoints_dir ./weights  --tensorboard_dir ./logs  --lr 0.0001  --lr_backbone 0.00001  --batch_size 8  --eval_freq 1  --gpu_id 0 --resume ./weights/latest.pth --start_epoch 5
'''
