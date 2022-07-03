# FreeCAD/Coin/Inventor support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

# import os; os.chdir("C:/svn/tangviz/proj/pivy.3/"); sys.path.append(".")

from pivyXi import *

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

imgFn    = 'c:/tmp/unsdg-transpWh01.png'
imgPlane = pxImagePlane(imgFn)

sg.addChild(imgPlane.getNode())
Gui.SendMsgToActiveView("ViewFit")

### end ###

