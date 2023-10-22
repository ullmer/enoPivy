# Enodia Coin Pivy support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy   import coin
from pivyXi import *

#################################################################
#################### Enodia Coin ImagePlane #####################

class pxImagePlane(pxNode):
  imgTexture     = None
  faceset        = None
  imgFn          = None
  imgCoord       = None

  #textureModel   = 'BLEND'
  textureModel   = 'MODULATE'

  facesetVals = [[-1, -1, 0], [1, -1, 0], 
                 [ 1,  1, 0], [-1, 1, 0]]

  facesetIdxs = [0, 1, 2, 3, -1]

  #################### constructor #####################

  def __init__(self, imgFn, **kwargs):
    super().__init__(kwargs)

    self.buildImagePlane(imgFn)

  #################### build Image Plane #####################

  def buildImagePlane(self, imgFn):

    self.imgFn                 = imgFn
    self.imgTexture            = coin.SoTexture2()

    if imgFn is not None: 
      self.imgTexture.filename = imgFn
    self.imgTexture.model      = self.textureModel

    self.imgCoord              = coin.SoCoordinate3()
    self.imgCoord.point.setValues(self.facesetVals)

    self.faceset = coin.SoIndexedFaceSet()
    self.faceset.coordIndex.setValues(self.facesetIdxs)

    children  = [self.imgTexture, self.imgCoord, self.faceset] 

    for child in children: self.node.addChild(child)

    return self.node

#################################################################
################# Enodia Coin ImagePlane Array (1D) #############

class pxImagePlaneArray (pxNode):
  cols      = None
  autobuild = True
  xoffset   = 1.1 
  
  #################### constructor #####################

  def __init__(self, imgFn, **kwargs):
    super().__init__(kwargs)

    if self.cols not None and self.autobuild:

#################################################################
################# Enodia Coin ImagePlane Grid (2D) ##############

class pxImagePlaneGrid(pxNode):
  rows      = None
  cols      = None
  autobuild = True
  xoffset   = 1.1 
  yoffset   = 1.1

  rowImagePlaneArrays = None

  #################### constructor #####################

  def __init__(self, imgFn, **kwargs):
    super().__init__(kwargs)

    if self.rows not None and self.cols not None and self.autobuild:
      self.buildGrid()
  
  #################### build grid #####################

  def buildGrid(self):
    if self.rows not None or self.cols not None:
      print("pivyXi pxImagePlaneGrid: rows and/or cols need vals (%s, %s)" % 
            (self.rows, self.cols))
      return None
    
    self.rowImagePlaneArrays = {}

    for i in self.rows:
      rowSep = new coin.SoSeparator()
      self.rowSeparators[i] = rowSep
      self.rowImagePlaneArrays = {}

      for j in self.cols:
        imgPlane = pxImagePlane() 
        
        
    
    children  = [self.imgTexture, self.imgCoord, self.faceset] 

    for child in children: self.node.addChild(child)

### end ###

