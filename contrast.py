from Utils import *
from IO import *

def accumulation(imageMatrix, ndG, nbLines, nbCols):
  h_cum = histogrammeCum(imageMatrix, ndG, nbLines, nbCols)
  A = [0] * (ndG+1)
  for i in range(0,ndG+1):
    pc = h_cum[i] / (nbLines*nbCols)
    A[i] = int((ndG-1) * pc)
  return A


def egalisation_histogram(imageMatrix, ndG, nbLines, nbCols):
  A = accumulation(imageMatrix, ndG, nbLines, nbCols)
  h = histogramme(imageMatrix, ndG, nbLines, nbCols)
  h_eg = [0]*(ndG+1)
  for i in range(0, ndG+1):
    h_eg[A[i]] = h_eg[A[i]] + h[i]
  return h_eg

def egalisation_histogram2(imageMatrix, ndG, nbLines, nbCols):
    histogrammecumm =  histogrammeCum(imageMatrix, ndG, nbLines, nbCols)
    LUT = [0] * (ndG + 1)
    n = nbLines * nbCols
    for i in range(0,ndG + 1):
        LUT[i] = int(ndG * histogrammecumm[i] / n)
    imageEqualised  = np.array(imageMatrix)
    for i in range(0,nbLines):
        for j in range(0,nbCols):
            imageEqualised[i][j] = LUT[imageMatrix[i][j]]
    return imageEqualised


def transformation_lineaire(imageMatrix, ndG, nbLines, nbCols,p1,p2):
  img = np.empty(imageMatrix.shape, dtype=int)
  for i in range(0,nbLines):
    for j in range(0,nbCols):
      if (imageMatrix[i, j] <p1[0]):
        a = p1[1]/p1[0]
        img[i,j] = int(a * imageMatrix[i, j])
      elif (imageMatrix[i,j] <p2[0]):
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p2[1]-a*p2[0]
        img[i,j] = int(a * imageMatrix[i, j] + b)
      else:
        a = (255 - p2[1]) / (255 - p2[0])
        b = 255 - 255 * a
        img[i, j] = int(a * imageMatrix[i, j] + b)
  return img.astype(dtype=int)