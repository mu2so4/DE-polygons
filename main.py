import sys
import os
import glob
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import geopandas as gpd
import csv

def read_polygon(filename):
	with open(filename) as inp_file:
		data = inp_file.readlines()
		coords = []
		for line in data:
			str_numbers = line.split()
			coords.append([float(s) for s in str_numbers])
	return Polygon(coords)


def write_shape(shape, name):
	with open(name + ".csv", "w") as out_file:
		if shape.is_empty:
			out_file.write("EMPTY POLYGON\n")
			return

		holes = list(shape.interiors)
		if len(holes) == 0:
			out_file.write("POLYGON\n")
		else:
			out_file.write("POLYGON WITH HOLES\n")

		writer = csv.writer(out_file, delimiter='\t')
		bound_coords = list(shape.exterior.coords)
		for point in bound_coords:
			writer.writerow(point)

		for hole in holes:
			out_file.write("\nhole\n")
			for point in list(hole.coords):
				writer.writerow(point)

		gpd.GeoSeries([shape]).plot()
		plt.savefig(name + ".png")


for f in glob.glob("*.png"):
	os.remove(f)

filename1 = sys.argv[1]
polygon1 = read_polygon(filename1)

filename2 = sys.argv[2]
polygon2 = read_polygon(filename2)
gpd.GeoSeries([polygon1, polygon2]).boundary.plot()
plt.savefig("initial_position.png")

mergedPolys = polygon1.union(polygon2)
write_shape(mergedPolys, "union")

intersectedPolys = polygon1.intersection(polygon2)
write_shape(intersectedPolys, "intersection")

diff_1_2 = polygon1.difference(polygon2)
write_shape(diff_1_2, "difference_1_without_2")

diff_2_1 = polygon2.difference(polygon1)
write_shape(diff_2_1, "difference_2_without_1")
