# Enodia Coin/Inventor example
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

# import os; os.chdir("C:/svn/tangviz/proj/pivy.3/"); sys.path.append(".")

from pivyXi import *

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
scene = pxNodes()

imgFn         = 'c:/tmp/unsdg-transpWh01.png'
depthImgStack = 5

for i in range(depthImgStack):
  imgPlane  = pxImagePlane(imgFn) 
  imgPlaneT = pxTranslate([0, 0, .5*i], imgPlane)
  scene.append(imgPlaneT)

scene.addToParent(sg)

Gui.SendMsgToActiveView("ViewFit")

### end ###

