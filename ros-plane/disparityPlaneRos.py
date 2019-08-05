#!/usr/bin/env python

import math
from readCameraConfig import CFG
import matplotlib.pyplot as plt
import cv2
import numpy as np
from scipy.spatial import ConvexHull
# from pyhull.convex_hull import ConvexHull as convex
# import pylab
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as patches
import os



def disparityPlane(leftImage, rightImage, configFilePath, name, SAVE=False):
    """
    :param leftImagePath:
    :param rightImagePath:
    :param configFilePath:
    :param varargi:
    :return:
    """

    assert name != None

    camraCfg = CFG(configFilePath)

    focal = camraCfg.focal
    baseline = camraCfg.baseline
    centerX = camraCfg.centerX
    centerY = camraCfg.centerY
    widthPixel = camraCfg.px_width
    heightPixel = camraCfg.px_height
    translation = camraCfg.translation
    rotationAngle = camraCfg.rotation * 180 / math.pi

    fx = focal * widthPixel
    fy = focal * heightPixel
    skew = 0

    meshStart = -0.5
    meshStep = 0.01
    meshEnd = 0.5

    imageLeft = leftImage
    imageRight = rightImage

    disparityRange = [0, 64]
    # numDisparities = 16
    window_size = 3
    min_disp = 64
    num_disp = 112 - min_disp

    # two stereo algorithms: BM and SGBM
    stereo_1 = cv2.StereoSGBM_create(minDisparity=0,
                                     numDisparities=num_disp,
                                     blockSize=19,
                                     P1=8 * 3 * window_size ** 2,
                                     P2=32 * 3 * window_size ** 2,
                                     disp12MaxDiff=1,
                                     uniquenessRatio=10,
                                     speckleWindowSize=100,
                                     speckleRange=32
                                     )

    stereo_2 = cv2.StereoBM_create(numDisparities=64, blockSize=19)  # TODO: not sure about those parameters
    imageDisparity = stereo_2.compute(imageLeft, imageRight).astype(np.float32) / 16  # has to have the image size
    # imageDisparity = cv2.normalize(imageDisparity, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F) # negative numbers are ok?

    imageLeftRows, imageLeftColumns = imageLeft.shape
    imageLeftTotalSize = imageLeftRows * imageLeftColumns  # 196608
    numMeasurements = int(imageLeftTotalSize / 100)

    randomizedIndexes = np.random.permutation(imageLeftTotalSize)
    randomizedIndexes = randomizedIndexes[:numMeasurements]

    # repmat(10, 3, 2) Create a 3-by-2 matrix whose elements contain the value 10.
    allIndexes_x = np.zeros(shape=(1, imageLeftTotalSize)).squeeze()
    allIndexes_y = np.zeros(shape=(1, imageLeftTotalSize)).squeeze()

    for indexRow in range(imageLeftRows):
        for indexColumn in range(imageLeftColumns):
            index = (indexColumn) * imageLeftRows + indexRow
            allIndexes_x[index] = indexRow  # allIndexes_x.squeeze()[index]
            allIndexes_y[index] = indexColumn

    vectorU = [allIndexes_y[i] for i in randomizedIndexes]
    vectorV = [allIndexes_x[i] for i in randomizedIndexes]
    vectorD = np.ones(shape=(1, numMeasurements))

    for index in range(numMeasurements):
       # print('the vectors are: ',vectorU[index], vectorV[index])
        vectorD[0, index] = imageDisparity[int(vectorV[index]), int(vectorU[index])]

    matrix_r1 = [np.multiply(vectorU, vectorU).sum(), np.multiply(vectorU, vectorD[0]).sum(), sum(vectorU)]
    matrix_r2 = [np.multiply(vectorU, vectorD[0]).sum(), np.multiply(vectorD[0], vectorD[0]).sum(), sum(vectorD[0])]
    matrix_r3 = [sum(vectorU), sum(vectorD[0]), numMeasurements]

    matrixTransposeATimesMatrixA = np.array([matrix_r1, matrix_r2, matrix_r3])
    matrixTransposeATimesVectorB = np.array(
       [np.multiply(vectorU, vectorV).sum(), np.multiply(vectorD[0], vectorV).sum(), sum(vectorV)])
    vectorXprime = np.linalg.lstsq(matrixTransposeATimesMatrixA, matrixTransposeATimesVectorB, rcond=-1)[0]

    # print('vectorXprime --->', vectorXprime)

    matrixInverseT = np.array([[1, 0, 0], [centerX / focal, 0, 1/focal], [0, baseline, 0]])
    # print(matrixInverseT)

    sec = np.subtract(vectorXprime, np.array([0, 0, centerY]))
    # print('sec --->', sec)
    vectorABC = np.matmul(matrixInverseT, sec)
    # print('vectorABC ---> ', vectorABC)
 #   vectorABC = np.array([0.234, -0.77842, 1.2344, 2.345])

    numValues = round((meshEnd - meshStart) / meshStep + 1)

    valuesX = np.linspace(-0.5, 0.5, 101)  # no meshStep,  101 is how many numbers should linspace output
    valuesZ = np.linspace(-0.5, 0.5, 101)
    valuesPlotZ, valuesPlotX = np.meshgrid(valuesZ, valuesX)

    valuesY = np.zeros(shape=(int(numValues), int(numValues)))

    # print(valuesX[4])
    for indexX in range(int(numValues)):
        for indexZ in range(int(numValues)):
            valuesY[indexX, indexZ] = vectorABC[0] * valuesX[indexX] + vectorABC[1] * valuesZ[indexZ] + vectorABC[2]



    intrinsicMatrix = np.array([[fx, 0, 0], [skew, fy, 0], [centerX, centerY, 1]])
    # print(intrinsicMatrix)

    cameraParams = intrinsicMatrix
    angleY = 0
    rotationY = np.array([[math.cos(np.radians(angleY)), 0, np.sin(np.radians(angleY))], [0, 1, 0],
                              [-np.sin(np.radians(angleY)), 0, math.cos(np.radians(angleY))]])

    angleX = -rotationAngle
    rotationX = np.array([[1, 0, 0], [0, math.cos(np.radians(angleX)), -np.sin(np.radians(angleX))],
                             [0, math.sin(np.radians(angleX)), math.cos(np.radians(angleX))]])

    angleZ = 0
    rotationZ = np.array([[math.cos(np.radians(angleZ)), -np.sin(np.radians(angleZ)), 0],
                            [np.sin(np.radians(angleZ)), math.cos(np.radians(angleZ)), 0], [0, 0, 1]])

    rotationMatrix = np.matmul(np.matmul(rotationX,rotationY),rotationZ)
    translationVector = np.array([0, 0, translation])
    # print(rotationMatrix)
    # print(translationVector)

    first = np.vstack((rotationMatrix, translationVector))

    camProjectionMatrix = np.matmul(first,intrinsicMatrix)
    euclidianPoint = []
    imageSpacePoints = [[] for i in range(int(numValues) * int(numValues))]
    # print(imageSpacePoints)
    # print(valuesZ)
    
    numValues = int(numValues) 

    for indexRow in range(numValues):
        for indexColumn in range(numValues):
            index = (indexColumn) * numValues + indexRow
            euclideanPoint = [valuesX[indexRow], valuesY[indexRow, indexColumn], valuesZ[indexColumn], 1];
            imageSpacePoints[index] = np.matmul(euclideanPoint, camProjectionMatrix)
            imageSpacePoints[index] = imageSpacePoints[index] / imageSpacePoints[index][2]
            # print(imageSpacePoints[index])

    # print(imageSpacePoints)
    matrixImageSpacePoints = np.array(imageSpacePoints)
    # print(len(matrixImageSpacePoints))

    imageSpacePointsX = matrixImageSpacePoints[:, 0]
    imageSpacePointsY = matrixImageSpacePoints[:, 1]

    # print(len(imageSpacePointsX))
    # print(len(imageSpacePointsY))

    points_ = np.column_stack((imageSpacePointsX, imageSpacePointsY))
    hull = ConvexHull(points_)

    # points for the patch
    x_patch = [imageSpacePointsX[i] for i in hull.vertices]
    y_patch = np.array([imageSpacePointsY[i] for i in hull.vertices])
    # print(f'the original X coordinates are {x_patch}')
    # print(f'the original Y coordinates are {y_patch}')

    # applying a sort of normalisation to the y coordinates and sort them
    y_patch = (y_patch / 4)  # TODO: y coordinates are much bigger the the height of the image
    # print(x_patch, y_patch)
    sorted_x = sorted(x_patch)
    sorted_y = sorted(y_patch)
    # print(f'the X coordinates are {sorted_x}')
    # print(f'the Y coordinates are {sorted_y}')
    
    
    return vectorABC
