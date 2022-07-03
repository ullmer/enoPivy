# Enodia Coin/Inventor example
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

# import os; os.chdir("/Users/bullmer/sp/pivy.3"); sys.path.append(".")
# import os; os.chdir("C:/svn/tangviz/proj/pivy.3/"); sys.path.append(".")

from pivyXi import *

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

scene = pxNodes()
#imgFn = '/Users/bullmer/sp/pivy.3/support/unsdg-transpWh01.png'
imgFn = 'c:/tmp/unsdg-transpWh01.png'
depthImgStack = 5

for i in range(depthImgStack):
  imgPlane  = pxImagePlane(imgFn) 
  imgPlaneT = pxTranslate([0, 0, .5*i], imgPlane)
  scene.append(imgPlaneT)

scene.addToParent(sg)

### Simple animation ###

def timerCb(data, sensor):
  global scene, depthImgStack
  for i in range(depthImgStack): scene.nudge(i, [0, .01*i, 0])

sts = coin.SoTimerSensor(timerCb, None)
sts.setInterval(.1)
sts.schedule()

Gui.SendMsgToActiveView("ViewFit")

### end ###

