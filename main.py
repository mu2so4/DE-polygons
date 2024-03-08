import matplotlib.pyplot as plt

input_file_name = "tests/1.txt"
input_file = open(input_file_name, "r")

with open(input_file_name) as file_inp:
	data = file_inp.readlines()
	coords = []
	for line in data:
		string_numbers = line.split()
		coords.append([float(s) for s in string_numbers])

input_file.close()

coords.append(coords[0])
xs, ys = zip(*coords)

plt.figure()
plt.plot(xs,ys)
plt.show()
