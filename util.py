from osgeo import ogr

def getData():
	driver = ogr.GetDriverByName('ESRI Shapefile')
	polyshp = driver.Open('/home/pcorti/data/shapefile/multipoly.shp')
	polylyr = polyshp.GetLayer(0)
	pointshp = driver.Open('/home/pcorti/data/shapefile/point.shp')
	pointlyr = pointshp.GetLayer(0)
	point = pointlyr.GetNextFeature()
	polygon = polylyr.GetNextFeature()

# if strata, the enveloppe is the strata bounding box
# bbox = minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
def randomDraw(number, bbox, strata = None):
	if strata is None:
		xyColl = [ [random.uniform(bbox[0], bbox[1]), random.uniform(bbox[2], bbox[3])] for ii in xrange(number)]
	else:
		xyColl = []
		ii = 0
		maxFail = 100
		fail = 0
		while ii < number and fail < maxFails:
			# draw in BBOX
			point = ogr.Geometry(ogr.wkbPoint)
			point.AddPoint( random.uniform(bbox[0], bbox[1]), random.uniform(bbox[2], bbox[3]) )
			if pointInPoly( point, strata ):
				xyColl.append( point )
				ii += 1
			else:
				fail += 1

def pointInEnvelop(point, polygon):
	minLong,maxLong,minLat,maxLat = geometry.GetEnvelope()
	if point.GetX() < minLong or point.GetX() > maxLong or point.GetY() < minLat or point.GetY() > maxLat:
		return False
	return True

def pointInPoly(point, polygon)
	return point.GetGeometryRef().Within(polygon.GetGeometryRef())

def xxxx():
	import osgeo.osr
	spatialReference = osgeo.osr.SpatialReference()
	spatialReference.SetWellKnownGeogCS('WGS84')