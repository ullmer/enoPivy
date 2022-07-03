# Enodia Coin/Inventor example
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

# import os; os.chdir("/Users/bullmer/sp/pivy.3"); sys.path.append(".")
# import os; os.chdir("C:/cygwin64/home/bullmer/git/pivy-xi/"); sys.path.append(".")

from pivyXi import *

sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

scene = pxNodes()
#imgFn = '/Users/bullmer/sp/pivy.3/support/unsdg-transpWh01.png'
imgFn = 'c:/tmp/unsdg-transpWh01.png'
depthImgStack = 5; direction = 1

for i in range(depthImgStack):
  imgPlane  = pxImagePlane(imgFn) 
  imgPlaneT = pxTranslate([0, 0, .5*i], imgPlane)
  scene.append(imgPlaneT)

scene.addToParent(sg)

### Simple animation ###

def timerAnimCb(data, sensor):
  global scene, depthImgStack, direction
  for i in range(depthImgStack): scene.nudge(i, [0, .01*i*direction, 0])

def timerFlipCb(data, sensor):
  global direction
  direction *= -1

sts1 = coin.SoTimerSensor(timerAnimCb, None)
sts1.setInterval(.1) #Update position every 1/10 seconds
sts1.schedule()

sts2 = coin.SoTimerSensor(timerFlipCb, None)
sts2.setInterval(4)  #Flip animation direction every 2 seconds
sts2.schedule()

Gui.SendMsgToActiveView("ViewFit")

### end ###

