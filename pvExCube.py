# FreeCAD/Coin/Inventor support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy import coin
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

color = coin.SoBaseColor()
color.rgb = (1, 0, 0)

cube = coin.SoCube()
node = coin.SoSeparator()
node.addChild(color)
node.addChild(cube)
sg.addChild(node)

### end ###

