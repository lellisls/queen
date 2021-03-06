import numpy as npy
import csv
from common import *
import matplotlib.pyplot as plt

with open('../results3.csv','rb') as csvfile:
	csvdata = csv.reader(csvfile,delimiter=',', quotechar='.')
	experiments = []
	identifiers = []
	count = 0
	for row in csvdata :
		if(count%500 == 0) :
			experiments.append([])
			identifiers.append(row[0:4])
			count = 0
		# print row[5]
		# print( identifiers[-1])
		# print( row[4] )
		experiments[-1].append(int(row[4]))
		count = count + 1
	# minimum = 10000
	# best = 0
	means = []
	f = open("stats.csv",'w')
	for i in range( 0, 180 ) :
		m = npy.mean(experiments[i])
		s = npy.std(experiments[i])
		# print(experiments[i])
		means.append(m)
		f.write("{}, {}, {}\n".format(",".join(identifiers[i]), m,s))
	f.close()
	csvfile.close()
	# print "Experiment[{}] = {}+-{}".format(best,minimum,npy.std(experiments[best]))
	# print "Best experiment: " + ", ".join(identifiers[best])
	plt.plot(means)
	plt.show()
