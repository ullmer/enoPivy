# Enodia Coin Pivy support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy import coin
#sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

#################################################################
#################### Enodia Coin ImagePlane #####################

class pxNode:
  node   = None

  #################### getNode #####################

  def getNode(self): return self.node

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

  def __init__(self, imgFn):
    self.buildImagePlane(imgFn)

  #################### build Image Plane #####################

  def buildImagePlane(self, imgFn):

    self.imgFn               = imgFn
    self.imgTexture          = coin.SoTexture2()
    self.imgTexture.filename = imgFn
    self.imgTexture.model    = self.textureModel

    self.imgCoord            = coin.SoCoordinate3()
    self.imgCoord.point.setValues(self.facesetVals)

    self.faceset = coin.SoIndexedFaceSet()
    self.faceset.coordIndex.setValues(self.facesetIdxs)

    self.node = coin.SoSeparator()
    children  = [self.imgTexture, self.imgCoord, self.faceset] 

    for child in children: self.node.addChild(child)

    return self.node

################################################################
#################### Enodia Coin translate #####################

class pxTranslate(pxNode):
  translateVal   = None
  translateEl    = None
  translatedNode = None
  
  #################### constructor #####################

  def __init__(self, translateVal, translatedNode):
    self.buildTranslate(translateVal, translatedNode)

  #################### constructor #####################

  def nudge(self, deltaTranslateVal):
    x,y,z    = self.translateVal
    dx,dy,dz = deltaTranslateVal
    self.translateVal = [x+dx, y+dy, z+dz]
    self.translateEl.translation.setValue(self.translateVal)

  #################### constructor #####################

  def buildTranslate(self, translateVal, translatedNode):
    self.node = coin.SoSeparator()
    self.translateVal = translateVal

    self.translateEl = coin.SoTranslation()
    self.translateEl.translation.setValue(translateVal)

    self.node.addChild(self.translateEl)
    self.node.addChild(translatedNode.getNode())
    self.translatedNode = translatedNode

#################################################################
#################### Enodia Coin ImagePlane #####################

class pxNodes(pxNode):
  childList = None
  parentSep = None

  #################### constructor #####################

  def __init__(self):
    self.node = coin.SoSeparator()
    self.childList = []
  
  #################### append #####################

  def append(self, childNode):
    self.childList.append(childNode)        # a class derived from pxNode
    self.node.addChild(childNode.getNode()) # the SoSeparator of said class

  #################### append #####################

  def extend(self, childNodes):
    for childNode in childNodes: self.append(childNode)
    
  #################### get, nudge #####################

  def get(self, idx): return self.childList[idx]

  def nudge(self, idx, deltaTranslate):
    child = self.get(idx)
    child.nudge(deltaTranslate)

  #################### addToParent #####################

  def addToParent(self, parentSeparator):
    self.parentSep = parentSeparator
    parentSeparator.addChild(self.node)

### end ###

