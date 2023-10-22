# Enodia Coin Pivy support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy    import coin
from enoPivy import *

#################################################################
#################### Enodia Coin ImagePlane #####################

class enoImagePlane(pxNode):
  imgTexture     = None
  faceset        = None
  imgFn          = None
  imgCoord       = None
  normalObj      = None
  normal         = [0, 0, 1.]
  transparency   = 0

  #textureModel   = 'BLEND'
  textureModel   = 'MODULATE'

  facesetVals = [[-1, -1, 0], [1, -1, 0], 
                 [ 1,  1, 0], [-1, 1, 0]]

  facesetIdxs = [0, 1, 2, 3, -1]

  #################### constructor #####################

  def __init__(self, **kwargs):
    super().__init__(kwargs)

    self.buildImagePlane()

  #################### build Image Plane #####################

  def buildImagePlane(self):
    try:
      self.imgTexture            = coin.SoTexture2()

      if self.imgFn is not None: 
        self.imgTexture.filename = self.imgFn
  
      if self.transparency != 0:
        self.
  
      self.imgTexture.model      = self.textureModel
  
      self.imgCoord              = coin.SoCoordinate3()
      self.imgCoord.point.setValues(self.facesetVals)
  
      self.normalObj  = coin.SoNormal()
      self.normalObj.normal.setValue(self.normal)
  
      self.faceset = coin.SoIndexedFaceSet()
      self.faceset.coordIndex.setValues(self.facesetIdxs)
  
      children  = [self.imgTexture, self.imgCoord, self.normalObj, self.faceset] 
  
      for child in children: self.node.addChild(child)
  
      return self.node
    except:
      print("enoImagePlane buildImagePlane exception:"); traceback.print_exc()
      return False

#################################################################
################# Enodia Coin ImagePlane Array (1D) #############

class enoImagePlaneArray(pxNode):
  cols       = None
  autobuild  = True
  offset     = [1.1, 0, 0]
  imgPlanes  = None
  planeTrans = None
  
  #################### constructor #####################

  def __init__(self, **kwargs):
    super().__init__(kwargs)

    if self.cols not None and self.autobuild:
      self.buildArray()

  #################### build array #####################

  def buildArray(self):
    try:
      if self.rows not None: 
        print("enoPivy enoImagePlaneArray: cols need vals (%s)" % self.cols)
        return None
      
      self.imgPlanes  = {}
      self.planeTrans = {}
  
      for i in self.cols:
        imgPlane = enoImagePlane() 
        imgNode  = imgPlane.getNode()
        imgTrans = coin.SbVec3f(self.offset)
  
        if i != 0: self.addChild(imgTrans)
        self.addChild(imgNode)
  
        self.imgPlanes[i] = imgPlane
        self.imgTrans[i]  = imgTrans
    except:
      print("enoImageArray buildArray exception:"); traceback.print_exc()
      return False

#################################################################
################# Enodia Coin ImagePlane Grid (2D) ##############

class enoImagePlaneGrid(pxNode):
  rows      = None
  cols      = None
  autobuild = True
  xoffset   = 1.1 
  yoffset   = 1.1
  offset    = [0, 1.1, 0]

  rowImagePlaneArrays = None
  rowTrans            = None

  #################### constructor #####################

  def __init__(self, **kwargs):
    super().__init__(kwargs)

    if self.rows not None and self.cols not None and self.autobuild:
      self.buildGrid(kwargs)
  
  #################### build grid #####################

  def buildGrid(self, **kwargs):
    try:
      if self.rows not None or self.cols not None:
        print("enoPivy enoImagePlaneGrid: rows and/or cols need vals (%s, %s)" % 
              (self.rows, self.cols))
        return None
      
      self.rowImagePlaneArrays = {}
      self.rowTrans            = {}
  
      for j in self.rows:
        imgPlaneArray = enoImagePlaneArray(kwargs) 
        self.rowImagePlaneArrays[j] = imgPlaneArray  
  
        arrayNode = imgPlaneArray.getNode()
        rowTrans  = coin.SbVec3f(self.offset)
  
        if i != 0: self.addChild(rowTrans)
        self.addChild(arrayNode)
  
        self.rowImagePlaneArrays [i] = imgPlaneArray
        self.rowTrans[i]             = rowTrans
    except:
      print("enoImageGrid buildGrid exception:"); traceback.print_exc()
      return False
    
### end ###

