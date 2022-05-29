from IO import *
from Utils import *
import random

def bruit(imageMatrix, ndG, nbLines, nbCols):
  noiseImage = np.array(imageMatrix)
  for lines in noiseImage:
    for cols in range(0,nbCols):
       n = random.randint(0,20)
       if(n == 0):
          lines[cols] = 0
       if(n == 20):
          lines[cols] = 255
  return noiseImage

def convolution(imageMatrix, ndG, nbLines, nbCols,filter,n):
  filtredImage = np.array(imageMatrix)
  for lines in range(0,nbLines):
    for cols in range(0,nbCols):
      convolution = 0
      for i in range(-n//2,(n//2)+ 1):
        if(((lines + i)>0) and ((lines + i)<nbLines)):
          for j in range((-n//2),(n//2)+1):
            if(((cols + j)>0) and ((cols + j)<nbCols)):
              convolution = convolution + imageMatrix[lines + i][cols + j]*filter[i + n//2][j + n//2]
      if convolution < 0:
        convolution = -convolution
      if convolution > ndG:
        convolution = ndG
      filtredImage[lines][cols] = convolution

  return filtredImage

def filtreMoyenne(n):
  filter = np.ones([n,n],dtype=int)
  filter = 1/(n**2) * filter
  return filter

def filterGaussian(n,sigma):
  gaussian = np.zeros((n, n))
  m = n//2
  for x in range(-m, m+1):
        for y in range(-m, m+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2 + y**2)/(2* sigma**2))
            gaussian[x+m, y+m] = (1/x1)*x2
  return gaussian

def filterMedian(imageMatrix, ndG, nbLines, nbCols,n):
  filtredImage = np.array(imageMatrix)
  for lines in range(0,nbLines):
    for cols in range(0,nbCols):
      medianArray = []
      for i in range(-n//2,(n//2)+ 1):
        if(((lines + i)>0) and ((lines + i)<nbLines)):
          for j in range((-n//2),(n//2)+1):
            if(((cols + j)>0) and ((cols + j)<nbCols)):
               medianArray.append(imageMatrix[lines + i][cols + j])
      medianArray = np.sort(medianArray)
      length = len(medianArray)
      filtredImage[lines][cols] = medianArray[length//2]
  return filtredImage

def filtrePasseHaut(type):
  if type == 1:
    return [[0,-1,0],[-1,5,-1],[0,-1,0]]
  elif type == 2:
    return [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]
  elif type == 3 :
    return [[1,-2,1],[-2,5,-2],[1,-2,1]]
  else :
    return None

