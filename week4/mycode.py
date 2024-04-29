import os
import cv2
import numpy as np

def visitDir(path):
    if not os.path.exists(path):
        print('Error:',path,'is not a directory or does not exist')
        return
    list_dirs=os.walk(path)
    for root, dirs, files in list_dirs:
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))
