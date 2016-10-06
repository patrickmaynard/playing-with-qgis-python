#Now I want to see whether I can print out all the names of my layer's features. 
#Adapted from ....
#    http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html
#    and
#    http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html 
#    and 
#    http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html#accessing-attributes

layerPluto = iface.addVectorLayer("/Users/patrickmaynard/Downloads/mn_mappluto_16v1/MNMapPLUTO.shp", "PLUTO", "ogr")
if not layerPluto:
  print "layerPluto failed to load!"
layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
if not layerEntrances:
  print "layerPluto failed to load!"

# Get the first feature from the layer
features = layerEntrances.getFeatures()
counter = 0
featuresSelected = []
for feature in features:
    # Print the feature name
    print feature['name']
    # Add the feature to our selection
    featuresSelected.append(feature.id())
    layerEntrances.setSelectedFeatures(featuresSelected)
