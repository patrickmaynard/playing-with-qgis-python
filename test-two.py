#Here I am just testing the ability to load a couple layers.
#Modified from http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html

layerPluto = iface.addVectorLayer("/Users/patrickmaynard/Downloads/mn_mappluto_16v1/MNMapPLUTO.shp", "PLUTO", "ogr")
if not layerPluto:
  print "layerPluto failed to load!"
  
layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
if not layerEntrances:
  print "layerPluto failed to load!"
