import math


def moyenne(imageMatrix, ndG, nbLines, nbCols):
    somme = 0
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            somme = somme + imageMatrix[i][j]
    return somme / (nbLines * nbCols)


def ecartType(imageMatrix, ndG, nbLines, nbCols):
    ecart = 0
    m = moyenne(imageMatrix, ndG, nbLines, nbCols)
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            ecart = ecart + ((imageMatrix[i][j] - m) ** 2)
    return math.sqrt(ecart / (nbLines * nbCols))


def histogramme(imageMatrix, ndG, nbLines, nbCols):
    histogramme = [0] * (ndG + 1)
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            histogramme[imageMatrix[i][j]] = histogramme[imageMatrix[i][j]] + 1
    return histogramme


def histogrammeCum(imageMatrix, ndG, nbLines, nbCols):
    histogrammeCum = [0] * (ndG + 1)
    h = histogramme(imageMatrix, ndG, nbLines, nbCols)
    histogrammeCum[0] = h[0]
    for i in range(1, ndG + 1):
        histogrammeCum[i] = histogrammeCum[i - 1] + h[i]
    return histogrammeCum


def RSB(imageMatrix, ndG, nbLines, nbCols, filtredImage):
    moy = moyenne(imageMatrix, ndG, nbLines, nbCols)
    s = 0
    b = 0
    for i in range(0, nbLines):
        for j in range(0, nbCols):
            s = s + (imageMatrix[i][j] - moy) ** 2
            b = b + (imageMatrix[i][j] - filtredImage[i][j]) ** 2
    if b == 0:
        return 1
    return math.sqrt(s / b)


def histogramme_normalise(imageMatrix, ndG, nbLines, nbCols):
    h = histogramme(imageMatrix, ndG, nbLines, nbCols)
    for i in range(0, len(h)):
        h[i] = h[i] / (nbLines * nbCols)
    return h


def variance_C1_C2(pC1, moy_C1, moy_C2, moy_image):
    return (pC1 * (moy_C1 - moy_image) ** 2) + ((1 - pC1) * (moy_C2 - moy_image) ** 2)
