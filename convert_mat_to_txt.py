# author : Baijun Feng
'''
Convert *.mat files to record annotations for imags in origin dataset to *.txt files.
'''

# load libraries
import scipy.io as sio
import numpy as np
import os

'''
# read single mat file to observe the structure
mat_filename = "./dataset/ShanghaiTech/part_A/train_data/ground-truth/GT_IMG_1.mat"
matdata = sio.loadmat(mat_filename)
# matdata = matdata['image_info'][0][0][0][0][0]
# matdata = matdata['image_info'][0][0][0][0][0][0] # get a list of two elements
matdata = matdata['image_info'][0][0][0][0][0]
print(matdata)

# txt_filename = mat_filename[0:len(mat_filename)-4] + ".txt" 
# print(txt_filename)
# savetxt_path =  txt_filename
# np.savetxt(savetxt_path, matdata, fmt="%0.8f")

'''

'''
all possible mat_dir_path and corresponding txt_dir_path:
"./dataset/ShanghaiTech/part_A/train_data/ground-truth/", "./dataset/ShanghaiTech/part_A/train_data/txt/"
"./dataset/ShanghaiTech/part_A/test_data/ground-truth/", "./dataset/ShanghaiTech/part_A/test_data/txt/"
"./dataset/ShanghaiTech/part_B/train_data/ground-truth/", "./dataset/ShanghaiTech/part_B/train_data/txt/"
"./dataset/ShanghaiTech/part_B/test_data/ground-truth/", "./dataset/ShanghaiTech/part_B/test_data/txt/"

'''

# enumerate *.mat files
mat_dir_path = "./dataset/ShanghaiTech/part_B/train_data/ground-truth/"
mat_filename_list = os.listdir(mat_dir_path)
# print(mat_filename_list)

txt_dir_path = "./dataset/ShanghaiTech/part_B/train_data/txt/"
if not os.path.exists(txt_dir_path):
    os.mkdir(txt_dir_path)
    print(f"make directory {txt_dir_path}")

cnt = 0
# convert *.mat files to *.txt files
for mat_filename in mat_filename_list:
    # print(mat_dir_path + mat_filename)
    matdata = sio.loadmat(mat_dir_path + mat_filename)
    data = matdata['image_info'][0][0][0][0][0]
    txt_filename = mat_filename[0:len(mat_filename)-4] + ".txt" 
    savetxt_path = txt_dir_path + txt_filename
    np.savetxt(savetxt_path, data, fmt="%0.8f") 
    cnt += 1
    if cnt % 100 == 0:
        print(f"processed {cnt} out of {len(mat_filename_list)}")

print("finishes!")