import sys
import matplotlib.pyplot as plt

def read_polynom(filename):
	with open(filename) as inp_file:
		data = inp_file.readlines()
		coords = []
		for line in data:
			str_numbers = line.split()
			coords.append([float(s) for s in str_numbers])
	coords.append(coords[0])
	return coords

filename1 = sys.argv[1]
polynom1 = read_polynom(filename1)
xs1, ys1 = zip(*polynom1)
#plt.figure()
plt.plot(xs1, ys1)

filename2 = sys.argv[2]
polynom2 = read_polynom(filename2)
xs2, ys2 = zip(*polynom2)
#plt.figure()
plt.plot(xs2, ys2)

plt.show()
