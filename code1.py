'''Importing modules'''

import numpy as np
import cv2
from scipy import ndimage as ndi


'''Function definitions'''

def gaborKernel():
    kernels = []
    ksize = 21
    j = 0
    for lamda in range(4):
        a = (1.9661)**(-2*lamda)
        for theta in np.arange(0, np.pi, np.pi / 6):
            kern = cv2.getGaborKernel((ksize, ksize), 1.0, theta, a, 1, 0, ktype=cv2.CV_32F)
            kern /= 1.5*kern.sum()
            kernels.append(kern)
        for i in range(0,6):
            kernels[j] += kernels[i + j]
        j = j+6
    
    temp = [0,0,0,0]
    for i in range(0,4):
        temp[i] = kernels[i]
    kernels = 0
    kernels = temp
    '''thefile = open('kernel.txt', 'w')
    for item in kernels:
        for items in item:
            thefile.write("%s\n" % items)'''
    return kernels

def compute_feats(image, kernels):
    feats = np.zeros((len(kernels), 2), dtype=np.double)
    for i in range(4):
        filtered = cv2.filter2D(image, cv2.CV_8UC3, kernels[i])
        '''cv2.imshow('filtered',filtered)
        cv2.waitKey(0)
        cv2.destroyAllWindows()'''
        feats[i, 0] = filtered.mean()/25600
        feats[i, 1] = filtered.std()/25600
    return feats


def match(feats, ref_feats):
    error = {}
    for i in range(0,112):
        for j in range(0,16):
            error[(i,j)] = np.sum((feats - ref_feats[i, j, :])**2)
    return error

def refFeats(k):
    kernels = k
    ref_feats = np.zeros((112, 16, 4, 2), dtype=np.double)
    for i in range(0,112):
        for j in range(0,16):
            img = cv2.imread('F:\Texture Classification Using Complex Wavelet Transform\Rotated Images\R' + str(i+1) + '-' + str(j+1) + '.tif',0)
            ref_feats[i, j, :, :] = compute_feats(img, kernels)
    thefile = open('kernel.txt', 'w')
    for item in ref_feats:
        for items in item:
            thefile.write("%s\n" % items)
    return ref_feats

def cfeats(x,k):
    i = int(x[0:3])
    j = int(x[3:5])
    i = i+1
    j = j+1
    kernels = k
    img1 = cv2.imread('F:\Texture Classification Using Complex Wavelet Transform\Rotated Images\R' + str(i) + '-' + str(j) + '.tif',0)
    feats = compute_feats(img1, kernels)
    return feats

def topprint(cmp1):
    i = 0
    for key, value in sorted(cmp1.iteritems(), key=lambda (k,v): (v,k)):
        if  i<21:
            print "%s: %s" % (key, value)
        i = i+1
''' gker = gaborKernel()
ref_feats = refFeats(gker)
img1 = cv2.imread('F:\Texture Classification Using Complex Wavelet Transform\Rotated Images\R' + str(20) + '-' + str(7) + '.tif',0)
feats = compute_feats(img1, gker)

cmp1 = match(feats, ref_feats)

for key, value in sorted(cmp1.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value) '''