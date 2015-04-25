import sys
from gene import genetic
from common import *

if(len(sys.argv) != 5) :
	print "Usage: " + sys.argv[0] + " <Population size> <Keep Rate 0:1> <Mutation Rate 0:1> <Max iterations>"
	exit(1);
populationSize = 2 * (int(sys.argv[1])/2) #Tamanho da populacao
keepRate = float(sys.argv[2]) #Taxa de genes mantidos a cada geracao
mutationRate = float(sys.argv[3]) #Taxa de mutacao
maxIterations = int(sys.argv[4]) #Numero maximo de iteracoes
# print "Genetic algorithm:\n\tPopulation Size = {}\n\tKeep rate = {}\n\tMutation rate = {}".format(populationSize,keepRate,mutationRate)

with open("genetic-compare.csv", "w") as file :
	for i in range(0,1000) :
		count, col = genetic( populationSize, keepRate, mutationRate, maxIterations )
		file.write("{}, {}\n".format(count, col))
# print "{}, {}, {}, {}, {}, {}, {}".format(populationSize,keepRate,crossRate,mutationRate,maxIterations,count,col)
#print( "{}, {}, {}, {}, {}, {}".format(populationSize,keepRate,mutationRate,maxIterations,count,col) +"\n")

print str(count) + " iterations."
print str(col) + " collision(s)."



