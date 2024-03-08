import sys
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.ops import unary_union
import geopandas as gpd

def read_polygon(filename):
	with open(filename) as inp_file:
		data = inp_file.readlines()
		coords = []
		for line in data:
			str_numbers = line.split()
			coords.append([float(s) for s in str_numbers])
	'''
	coords.append(coords[0])
	return coords
	'''
	return Polygon(coords)

filename1 = sys.argv[1]
polygon1 = read_polygon(filename1)
#xs1, ys1 = zip(*polygon1)
#plt.figure()
#plt.plot(xs1, ys1)

filename2 = sys.argv[2]
polygon2 = read_polygon(filename2)
#xs2, ys2 = zip(*polygon2)
#plt.figure()
#plt.plot(xs2, ys2)
polys = [polygon1, polygon2]

mergedPolys = unary_union(polys)
gpd.GeoSeries([mergedPolys]).boundary.plot()
plt.show()

