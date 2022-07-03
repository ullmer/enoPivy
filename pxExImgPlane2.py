# FreeCAD/Coin/Inventor support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

# import os; os.chdir("C:/svn/tangviz/proj/pivy.3/"); sys.path.append(".")

from pivyXi import *

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
scene = pxNodes()

imgFn = 'c:/tmp/unsdg-transpWh01.png'
imgPl1  = pxImagePlane(imgFn) #first instance of image
imgPl2  = pxImagePlane(imgFn) #second instance of image
imgPl2t = pxTranslate([0, 0, -1], imgPl2)

nodes = [imgPl1, imgPl2t]
scene.extend(nodes)
scene.addToParent(sg)

Gui.SendMsgToActiveView("ViewFit")

### end ###

