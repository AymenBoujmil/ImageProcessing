from Utils import *
import numpy as np


def binarisation(imageMatrix, ndG, nbLines, nbCols):
    imageBin = np.array(imageMatrix)
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            if imageMatrix[i][j] > ((imageMatrix.min() + imageMatrix.max()) / 2):
                imageBin[i][j] = ndG
            else:
                imageBin[i][j] = 0
    return imageBin


def dilatation(imageMatrix, ndG, nbLines, nbCols, n):
    imageBin = np.array(imageMatrix)
    for i in range(0, nbLines):
        for j in range(0,nbCols):
            dilatation = []
            for x in range(max(0, i - n // 2), min(nbLines, i + n // 2 + 1)):
                for y in range(max(0, j - n // 2), min(nbCols, j + n // 2 + 1)):
                    dilatation.append(imageMatrix[x][y])
            dilatation.sort()
            imageBin[i][j] = dilatation[0]
    return imageBin


def erosion(imageMatrix, ndG, nbLines, nbCols, n):
    imageBin = np.array(imageMatrix)
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            erosion = []
            for x in range(max(0, i - n // 2), min(nbLines, i + n // 2 + 1)):
                for y in range(max(0, j - n // 2), min(nbCols, j + n // 2 + 1)):
                    erosion.append(imageMatrix[x][y])
            erosion.sort()
            imageBin[i][j] = erosion[len(erosion) - 1]
    return imageBin


def fermeture(imageMatrix, ndG, nbLines, nbCols, n):
    return erosion(dilatation(imageMatrix, ndG, nbLines, nbCols, n), ndG, nbLines, nbCols, n)

def ouverture(imageMatrix, ndG, nbLines, nbCols, n):
    return dilatation(erosion(imageMatrix, ndG, nbLines, nbCols, n), ndG, nbLines, nbCols, n)

