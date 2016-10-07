#Now I want to see whether I can print out x/y coordinates for each of a few addresses. 
#Adapted from http://gis.stackexchange.com/questions/209292/getting-x-y-of-polygon-in-pyqgis

#layerPluto = iface.addVectorLayer("/Users/patrickmaynard/Downloads/mn_mappluto_16v1/MNMapPLUTO.shp", "PLUTO", "ogr")
if not layerPluto:
  print "layerPluto failed to load!"
#layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
if not layerEntrances:
  print "layerPluto failed to load!"

#features = layerEntrances.getFeatures()
features = layerPluto.getFeatures()
counter = 0
featuresSelected = []
for feature in features:
    if counter < 3:
        #print feature['name']
        print feature['Address']
        print feature.geometry().centroid().asPoint().x()
        print feature.geometry().centroid().asPoint().y()
        featuresSelected.append(feature.id())
        layerEntrances.setSelectedFeatures(featuresSelected)
    counter += 1
