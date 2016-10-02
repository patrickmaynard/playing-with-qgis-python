#Here I am just testing the ability to load a layer.
#Modified from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html

layer = iface.addVectorLayer("/Users/patrickmaynard/Downloads/mn_mappluto_16v1/MNMapPLUTO.shp", "PLUTO", "ogr")
if not layer:
  print "Layer failed to load!"
