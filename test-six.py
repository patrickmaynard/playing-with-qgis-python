#Now I want to see whether I can print out lat/lon coordinates for each of a few addresses. 
#Adapted from http://gis.stackexchange.com/questions/209292/getting-x-y-of-polygon-in-pyqgis
#... and http://gis.stackexchange.com/questions/213426/converting-pluto-coordinate-reference-system-in-qgis/213537#213537

layerPluto = iface.addVectorLayer("/Users/patrickmaynard/Desktop/delete-me-soon/new-crs.shp", "PLUTO", "ogr")
if not layerPluto:
  print "layerPluto failed to load!"
layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
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
        print feature.geometry().centroid().asPoint().y()
        print feature.geometry().centroid().asPoint().x()
        featuresSelected.append(feature.id())
        layerEntrances.setSelectedFeatures(featuresSelected)
    counter += 1
