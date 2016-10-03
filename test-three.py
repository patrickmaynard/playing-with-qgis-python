#Now I want to see whether I can select a single feature from a given layer. 
#Adapted from ....
#    http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html
#    and
#    http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html 

layerPluto = iface.addVectorLayer("/Users/patrickmaynard/Downloads/mn_mappluto_16v1/MNMapPLUTO.shp", "PLUTO", "ogr")
if not layerPluto:
  print "layerPluto failed to load!"
layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
if not layerEntrances:
  print "layerPluto failed to load!"

# Get the first feature from the layer
feature = layerEntrances.getFeatures().next()
# Get the first feature from the layer
ayerEntrances.setSelectedFeatures([feature.id()])
