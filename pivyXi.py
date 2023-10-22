# Enodia Coin Pivy support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy import coin
#sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

#######################################################
#################### Pivy Xi node #####################

class pxNode:
  nodeSeparator = None

  #################### constructor #####################

  def __init__(self, imgFn, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.initNodeSeparator()

  #################### initialize node separator #####################

  def initNodeSeparator(self): 
    self.nodeSeparator = coin.SoSeparator()

  #################### getNode #####################

  def getNode(self): return self.nodeSeparator

################################################################
#################### Pivy Xi translate #####################

class pxTranslate(pxNode):
  translateVal   = None
  translateEl    = None
  translatedNode = None
  
  #################### constructor #####################

  def __init__(self, imgFn, **kwargs):
    self.__dict__.update(kwargs) #allow class fields to be passed in constructor
    #https://stackoverflow.com/questions/739625/setattr-with-kwargs-pythonic-or-not

    self.buildTranslate(self.translateVal, self.translatedNode)

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

