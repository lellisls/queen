import sys
from gene import genetic
from common import *

# if(len(sys.argv) != 6) :
# 	print "Usage: " + sys.argv[0] + " <Population size> <Keep Rate 0:1> <Cross Rate 0:1> <Mutation Rate 0:1> <Max iterations>"
# 	exit(1);
# populationSize = 2 * (int(sys.argv[1])/2) #Tamanho da populacao
# keepRate = float(sys.argv[2]) #Taxa de genes mantidos a cada geracao
# crossRate = float(sys.argv[3]) #Taxa de cruzamento
# mutationRate = float(sys.argv[4]) #Taxa de mutacao
# maxIterations = int(sys.argv[5]) #Numero maximo de iteracoes

# print "Genetic algorithm:\n\tPopulation Size = {}\n\tCross Rate = {}\n\tMutation rate = {}".format(populationSize,Gene.crossRate,Gene.mutationRate)
maxIterations = 1000
results = open('results.csv', 'w')
stats = open('stats.csv', 'w')
for populationSize in [10,30,50,80,100,250,500,750,1000] :
	for keepRate in [ 0.25, 0.5, 0.75, 1.0 ] :
		for crossRate in [ 0, 0.25, 0.5, 0.75, 1.0 ] :
			for mutationRate in [ 0, 0.25, 0.5, 0.75, 1.0 ] :
				counts = []
				cols = []
				for experiment in range(0,100) :
					count, col = genetic( populationSize, keepRate, crossRate, mutationRate, maxIterations )
					# print "{}, {}, {}, {}, {}, {}, {}".format(populationSize,keepRate,crossRate,mutationRate,maxIterations,count,col)
					results.write( "{}, {}, {}, {}, {}, {}, {}".format(populationSize,keepRate,crossRate,mutationRate,maxIterations,count,col) +"\n")
					counts.append(count)
					cols.append(int(col != 0))
					m = mean(counts)
					s = std(counts, m)
					m2 = mean(cols)
					s2 = std(cols,m2)
				print("{}, {}, {}, {}, {}, {}, {}, {}, {}".format( populationSize, keepRate, crossRate, mutationRate, maxIterations, m, s, m2, s2 ))
				stats.write(  "{}, {}, {}, {}, {}, {}, {}, {}, {}".format( populationSize, keepRate, crossRate, mutationRate, maxIterations, m, s, m2, s2 ) + "\n")
results.close()
stats.close()

