import math
import csv

#Now I want to write a sample csv file with the distances between a few properties and their closest subway stations.
#Inspired by http://iquantny.tumblr.com/post/99544282749/found-the-manhattan-apartment-thats-the-farthest 
#For full documentation of the people/threads/tutorials that helped lead to this project, please view the python comments in these scripts:
#https://github.com/patrickmaynard/playing-with-qgis-python

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    km = 6367 * c
    return km

def calculateDistance(featureProperty, layerEntrances):
    #This is a stub for what will eventually be our distance-to-closest-station function.
    shortestDistance = 1000
    featuresEntrances = layerEntrances.getFeatures()
    for featureEntrance in featuresEntrances:
            latEntrance = featureEntrance.geometry().centroid().asPoint().y()
            lonEntrance = featureEntrance.geometry().centroid().asPoint().x()
            latProperty = featureProperty.geometry().centroid().asPoint().y()
            lonProperty = featureProperty.geometry().centroid().asPoint().x()
            currentDistance = haversine(lonEntrance, latEntrance, lonProperty, latProperty)
            if currentDistance < shortestDistance:
                shortestDistance = currentDistance
    return shortestDistance

def importAndAnalyze(rowLimit = 3):
    layerProperties = iface.addVectorLayer("/Users/patrickmaynard/Desktop/delete-me-soon/new-crs.shp", "Properties", "ogr")
    if not layerProperties:
      print "layerProperties failed to load!"
    layerEntrances = iface.addVectorLayer("/Users/patrickmaynard/Downloads/subway/geo_export_950003d9-f387-479c-9bf5-a1ca5a252bce.shp", "Entrances", "ogr")
    if not layerEntrances:
      print "layerProperties failed to load!"
    features = layerProperties.getFeatures()
    counter = 0
    featuresSelected = []
    with open('/Users/patrickmaynard/Desktop/eggs.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        spamwriter.writerow(['Address', 'Lat','Lon', 'Distance'])
        for feature in features:
            if counter < rowLimit:
                #print feature['name']
                print feature['Address']
                spamwriter.writerow([feature['Address'], feature.geometry().centroid().asPoint().y(),feature.geometry().centroid().asPoint().x(), calculateDistance(feature, layerEntrances)])
                featuresSelected.append(feature.id())
                layerEntrances.setSelectedFeatures(featuresSelected)
            counter += 1
        
importAndAnalyze()
