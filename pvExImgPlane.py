# FreeCAD/Coin/Inventor support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy import coin
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

tex = coin.SoTexture2()
tex.filename = 'c:/tmp/unsdg-transpWh01.png'
tex.model    = 'BLEND'

coord1 = coin.SoCoordinate3()
coord1.point.setValues([[-1, -1, 0], [1, -1, 0], 
                        [ 1,  1, 0], [-1, 1, 0]])

pl1 = coin.SoIndexedFaceSet()
pl1.coordIndex.setValues([0, 1, 2, 3, -1])

node = coin.SoSeparator()
for child in [tex, coord1, pl1]: node.addChild(child)

sg.addChild(node)
Gui.SendMsgToActiveView("ViewFit")

### end ###

