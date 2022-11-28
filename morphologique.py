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


def calcul_probab_C1(imageMatrix, ndG, nbLines, nbCols, k, h, h_normalise):
    pC1 = 0
    moy = 0
    for i in range(0, k + 1):
        pC1 = pC1 + h_normalise[i]
        moy = moy + h[i]
    moy2 = (nbLines * nbCols - moy) / (255 - k)
    moy = moy / k + 1
    return pC1, moy, moy2


def find_k(imageMatrix, ndG, nbLines, nbCols):
    h = histogramme(imageMatrix, ndG, nbLines, nbCols)
    h_norm = histogramme_normalise(imageMatrix, ndG, nbLines, nbCols)
    moy_image = moyenne(imageMatrix, ndG, nbLines, nbCols)
    k = 1
    pC1, moy_C1, moy_C2 = calcul_probab_C1(imageMatrix, ndG, nbLines, nbCols, 1, h, h_norm)
    min = variance_C1_C2(pC1, moy_C1, moy_C2, moy_image)
    for i in range(2, 255):
        pC1, moy_C1, moy_C2 = calcul_probab_C1(imageMatrix, ndG, nbLines, nbCols, i, h, h_norm)
        variance = variance_C1_C2(pC1, moy_C1, moy_C2, moy_image)
        if variance < min:
            k = i
            min = variance
    return k


def seuillage_auto(imageMatrix, ndG, nbLines, nbCols):
    image_seuil = find_k(imageMatrix, ndG, nbLines, nbCols)
    image_seuille = np.empty((nbLines, nbCols), dtype=int)
    for line in range(0, nbLines):
        for col in range(0, nbCols):
            image_seuille[line, col] = 0 if imageMatrix[line, col] < image_seuil else 255
    return image_seuille


def dilatation(imageMatrix, ndG, nbLines, nbCols, n):
    imageBin = np.array(imageMatrix)
    for i in range(0, nbLines):
        for j in range(0, nbCols):
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
