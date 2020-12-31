import os
import cv2
import numpy as np
from tqdm import tqdm
import argparse
import fileinput

# function that turns XMin, YMin, XMax, YMax coordinates to normalized yolo format
def convert(filename_str, coords):
    os.chdir("..")
    image = cv2.imread(filename_str + ".jpg")
    xmin= coords[0]
    ymin= coords[1]
    xmax = coords[2]
    ymax = coords[3]
    
    coords[0] = ymin
    coords[1] = xmin
    coords[2] = ymax
    coords[3] = xmax
    os.chdir("Label")
    return coords

ROOT_DIR = os.getcwd()

# create dict to map class names to numbers for yolo
classes = {}
with open("classes.txt", "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num
    myFile.close()
# step into dataset directory
os.chdir(os.path.join("OID", "Dataset"))
DIRS = os.listdir(os.getcwd())

# for all train, validation and test folders
for DIR in DIRS:
    if os.path.isdir(DIR):
        os.chdir(DIR)
        print("Currently in subdirectory:", DIR)
        
        CLASS_DIRS = os.listdir(os.getcwd())
        # for all class folders step into directory to change annotations
        for CLASS_DIR in CLASS_DIRS:
            if os.path.isdir(CLASS_DIR):
                os.chdir(CLASS_DIR)
                print("Converting annotations for class: ", CLASS_DIR)
                num=0;
                # Step into Label folder where annotations are generated
                os.chdir("Label")

                for filename in tqdm(os.listdir(os.getcwd())):
                    filename_str = str.split(filename, ".")[0]# 이름그대로 가지고 오는거
                    if filename.endswith(".txt"):
                        annotations = []
                        with open(filename) as f:
                            for line in f:
                                for class_type in classes:
                                    line = line.replace(class_type, str(classes.get(class_type)))
                                labels = line.split()
                                coords = np.asarray([float(labels[2]), float(labels[3]), float(labels[4]), float(labels[5])])
                                coords = convert(filename_str, coords)
                                #한 이쪽 즈음에서 이 사진이 clockewise인지, clockwise_lr인지. clockwise_ud인지, clcokewise_ud_lr인지에 따라 좌표 바뀌는거 달라짐
                                labels[2], labels[3], labels[4], labels[5] = coords[0], coords[1], coords[2], coords[3]
                                newline = str(labels[0]) + " " + str(labels[1]) + " " + str(labels[2]) + " " + str(labels[3]) + " " + str(labels[4])+ " " + str(labels[5])
                                line = line.replace(line, newline)
                                annotations.append(line)
                            f.close()
                        os.chdir("Label_90")
                        with open(filename_str+"_90_lr.txt", "w") as outfile:
                            for line in annotations:
                                outfile.write(line)
                                outfile.write("\n")
                            outfile.close()
                            num=num+1;
                        os.chdir("..")
                os.chdir("..")
                os.chdir("..")
        os.chdir("..")
