import numpy as np


def readImageAscii(fileName):
    file = open(fileName, 'rb')
    imageType = file.readline().decode().strip('\n')
    if (imageType != "P5"):
        file.close()
        raise Exception
    else:
        while (True):
            line = file.readline().decode().strip('\n')
            if (line[0] != '#'):
                break
        (M, N) = line.split(" ")
        nbCols = int(M)
        nbLines = int(N)
        ndG = int(file.readline().decode().strip('\n'))
        image = []
        for line in file.readlines():
            for number in line.decode().split():
                image.append(int(number))
        if (len(image) != nbLines * nbCols):
            raise Exception
        imageMatrix = np.reshape(np.array(image), (nbLines, nbCols))
        return imageMatrix, ndG, nbLines, nbCols

def readImage(fileName):
   file = open(fileName, 'r')
   imageType = file.readline().strip('\n')
   if(imageType != "P2"):
      file.close()
      raise Exception
   else:
      while(file.readline()):
        line=file.readline().strip('\n')
        if(line[0]!='#') :
          break
      (M,N)=line.split(" ")
      nbCols = int(M)
      nbLines = int(N)
      ndG=int(file.readline().strip('\n'))
      image = []
      for line in file.readlines():
        for number in line.split():
          image.append(int(number))
      if(len(image)!= nbLines*nbCols):
        raise Exception
      imageMatrix = np.reshape(np.array(image),(nbLines,nbCols))
      return imageMatrix, ndG, nbLines, nbCols

def writeImage(fileName,imageMatrix, ndG, nbLines, nbCols):
  file = open(fileName, 'w')
  file.write("P2\n")
  file.write("#\n")
  file.write(str(nbCols) + " " + str(nbLines) + "\n")
  file.write(str(ndG)+"\n")
  for lines in imageMatrix:
    for cols in range(0,nbCols):
      file.write(str(lines[cols]) + " ")
    file.write("\n")
  file.close()