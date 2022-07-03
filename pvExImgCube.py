# FreeCAD/Coin/Inventor support routines 
# Brygg Ullmer, Clemson University
# Begun 2022-07-02

from pivy import coin
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()

tex = coin.SoTexture2()
tex.filename = 'c:/tmp/unsdg-transpWh01.png'
tex.model    = 'BLEND' #'MODULATE'

cube = coin.SoCube()
node = coin.SoSeparator()
node.addChild(tex)
node.addChild(cube)
sg.addChild(node)

### end ###

