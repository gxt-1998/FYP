# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 18:35:18 2019

@author: 37112
"""

import os
path = '/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/picture/'
#impath = 'E:/course/6680/ead2019_trainingData-I/ead2019_trainingData-I/train_release2_task1/image/'
#anpath = 'E:/course/6680/ead2019_trainingData-I/ead2019_trainingData-I/train_release2_task1/annotation/'
f = os.listdir(path)
#p = os.listdir(impath)
#print(p)
#a = os.listdir(anpath)
#print(a)
n = 0
for i in f:
    oldname = path + f[n]
    newname = path +'000'+ str(n) + '.jpg'
    os.rename(oldname,newname)
    n += 1
    print(newname)
# =============================================================================
# 
# for i in range(0,1305):
#     oldname1 = impath + p[n]
#     oldname2 = anpath + a[n]
# #    newname1 = impath +'000000'+ str(n+1) + '.jpg'
# #    newname2 = anpath +'000000'+ str(n+1) + '.txt'
#     if n < 113:
#         newname1 = impath +'000'+ str(n+887) + '.jpg'
#         newname2 = anpath +'000'+ str(n+887) + '.txt'
#     else:
#         newname1 = impath +'00'+ str(n+887) + '.jpg'
#         newname2 = anpath +'00'+ str(n+887) + '.txt'
#     os.rename(oldname1,newname1)
#     os.rename(oldname2,newname2)
#     n += 1
# =============================================================================
