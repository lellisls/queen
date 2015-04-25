import numpy as npy
import csv
import sys
from common import *
import matplotlib.pyplot as plt
if(len(sys.argv) != 2) :
	print "usage {} <csv file>".format(argv[0])

filename = sys.argv[1]

with open(filename,'rb') as csvfile:
	csvdata = csv.reader(csvfile,delimiter=',', quotechar='.')
	steps = []
	collisions = []
	errors = []
	success = []
	fails = []
	for row in csvdata :
		steps.append(int(row[0]))
		collisions.append(int(row[1]))
		if int(row[1]) != 0 :
			errors.append( 100 )
			fails.append(int(row[0]))
		else :
			errors.append( 0 )
			success.append(int(row[0]))
		# print row[5]
		# print( identifiers[-1])
	print "Steps = {} +- {}".format( npy.mean(steps), npy.std(steps) )
	print "Steps to success = {} +- {}".format( npy.mean(success), npy.std(success) )
	print "Steps to fail = {} +- {}".format( npy.mean(fails), npy.std(fails) )
	print "Collisions = {} +- {}" .format( npy.mean(collisions), npy.std(collisions) )
	print "Error ratio = {}% +- {}" .format( npy.mean(errors), npy.std(errors) )
	# minimum = 10000
	# best = 0
	# print "Experiment[{}] = {}+-{}".format(best,minimum,npy.std(experiments[best]))
	# print "Best experiment: " + ", ".join(identifiers[best])
	# plt.plot(steps)
	# plt.show()
