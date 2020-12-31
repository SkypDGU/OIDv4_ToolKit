import os
import glob
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput
'''
1.시계방향 90도
2.시계방향 90도에대한 상하반전 
3.좌우 반전 
4.상하 좌우반전


'''

path = './OID/Dataset/train/Human body/'  # 이미지 파일이 있는 경로 입력 EX. ./img
path = path + '/*.jpg'
images_list = glob.glob(path)

output_path = './OID/Dataset/train/Person_90/' # 회전된 이미지 파일이 저장될 경로



for img_path in tqdm(images_list):
    #print(img_path)
    img = cv2.imread(img_path)
    filename_str=os.path.basename(img_path)
    #print(filename_str)
    filename_str = str.split(filename_str, ".")[0]# 이름그대로 가지고 오는거
    #print(filename_str)

    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # 시계 방향 회전
    out_ = output_path +filename_str+'_90.jpg'
    cv2.imwrite(out_, img_rotate_90_clockwise)

    # 시계방향 회전에 대한
    img_clockwise_ud = cv2.flip(img_rotate_90_clockwise, 0)  # 상하 반전
    out_ = output_path +filename_str+'_90_ud.jpg'
    cv2.imwrite(out_, img_clockwise_ud)

    img_clockwise_lr = cv2.flip(img_rotate_90_clockwise, 1)  # 좌우반전
    out_ = output_path +filename_str+'_90_lr.jpg'
    cv2.imwrite(out_, img_clockwise_lr)

    img_clockwise_ud_lr = cv2.flip(img_rotate_90_clockwise, -1)  # 상하 좌우 반전
    out_ = output_path +filename_str+'_90_udlr.jpg'
    cv2.imwrite(out_, img_clockwise_ud_lr)



