import sys
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import geopandas as gpd

def read_polygon(filename):
	with open(filename) as inp_file:
		data = inp_file.readlines()
		coords = []
		for line in data:
			str_numbers = line.split()
			coords.append([float(s) for s in str_numbers])
	return Polygon(coords)

filename1 = sys.argv[1]
polygon1 = read_polygon(filename1)

filename2 = sys.argv[2]
polygon2 = read_polygon(filename2)

mergedPolys = polygon1.union(polygon2)
gpd.GeoSeries([mergedPolys]).plot()
plt.savefig("union.png")
print(mergedPolys)

intersectedPolys = polygon1.intersection(polygon2)
gpd.GeoSeries([intersectedPolys]).plot()
plt.savefig("intersection.png")
print(intersectedPolys)

diff_1_2 = polygon1.difference(polygon2)
gpd.GeoSeries([diff_1_2]).plot()
plt.savefig("difference_1_2.png")
print(diff_1_2)

diff_2_1 = polygon2.difference(polygon1)
gpd.GeoSeries([diff_2_1]).plot()
plt.savefig("difference_2_1.png")
print(diff_2_1)
