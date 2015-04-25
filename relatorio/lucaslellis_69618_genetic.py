import sys
from common import *

from common import *
import random
import math

class Gene ( object ):
  data = []
  fitness = int(0)
  crossRate = float(0)
  mutationRate = float(0)
  keepRate = float(0)
  board_size = 8 #Numero de genes
  bits_size = int(math.ceil(math.log(board_size-1))) + 1
  max_fitness = board_size * (board_size - 1)/2

  def __init__ (self, data) :
    self.data = data

  def __str__(self) :
    return "<{} {} >".format(self.data,self.fitness)

  def __repr__(self) :
    return "<{} {}>".format(self.data,self.fitness)

  def __lt__(self, other):
    return self.fitness < other.fitness

  def calcFitness( self ):
    self.fitness = Gene.max_fitness - collisions(self.data)

  def mutate( self ) :
    # if(random.randint(1,100) <= Gene.mutationRate ) :
    pos = random.randint(0,Gene.board_size-1)
    r = self.data[pos]
    while r == self.data[pos] :
      r = random.randint(0,Gene.board_size-1)
    self.data[pos] = r

  # def mutate( self ) :
  #   pos = random.randint(0,(Gene.board_size-1)*Gene.bits_size)
  #   bdata = decimal_to_bin(self.data)
  #   bdata[pos] = not( bdata[pos] )
  #   self.data = bin_to_decimal(bdata)
  def crossover( self, other, k ) :
     #k = random.randint(0,Gene.board_size -1)
    if(Gene.board_size != len(other.data)) :
      print ("Invalid input: self.data and other.data have different sizes.")
    if( Gene.board_size < k ) :
      print ("Invalid input: k > self.data size.")

    dec1 = Gene(self.data[0:k] + other.data[k:])
    dec2 = Gene(other.data[0:k] + self.data[k:])

    return ( dec1, dec2 )

  # def crossover( self, other) :
  #   k = random.randint(0,Gene.bits_size*(Gene.board_size -1))
  #   if( len(self.data * Gene.bits_size) < k ) :
  #     print "Invalid input: k > self.data size."
  #   if(k%Gene.bits_size == 0) :
  #     dec1 = Gene(self.data[0:k/Gene.bits_size] + other.data[k/Gene.bits_size:])
  #     dec2 = Gene(other.data[0:k/Gene.bits_size] + self.data[k/Gene.bits_size:])
  #   else :
  #     v1 = decimal_to_bin(self.data)
  #     v2 = decimal_to_bin(other.data)
  #     dec1 = Gene(bin_to_decimal(v1[0:k] + v2[k:]))
  #     dec2 = Gene(bin_to_decimal(v2[0:k] + v1[k:]))
  #   return ( dec1, dec2 )

# --------------------------------------------------------------------------------------------------------------------------------- #

# def select(population) :
#   wheel = []
#   for i in population :
#     for j in range(0,i.fitness) :
#       wheel.append(i)
#   res   = random.choice(wheel)
#   res2 = random.choice(wheel)
#   while res == res2 :
#     res2 = random.choice(wheel)
#   return (res, res2)

def select(population) :
  res = random.choice(population)
  res2 = random.choice(population)
  while( res == res2 ) :
    res2 = random.choice(population)
  return( res, res2 )

def fillPopulation(population, populationSize) :
  while len(population) < populationSize :
    population.append( Gene(generate(Gene.board_size)) )

def sortPopulation( population ) :
  population.sort(reverse=True)

def updateFitness(population) :
  for ind in population :
    ind.calcFitness()

def binary( n ) :
  if(n >= Gene.board_size) :
    print ("Invalid value: {}" .format(n))
  expr = "{0:0" + str(Gene.bits_size ) + "b}"
  res = [int(x) for x in list(expr.format(n))]
  # print "input = {}, output = {}" .format(n,res)
  return res

def decimal( b ) :
  res = 0
  for pos in range( 0, Gene.bits_size) :
    res = res + b[pos] * pow(2,Gene.bits_size - pos -1)
  # print "input = {}, output = {}" .format(b,res)
  return res

def bin_to_decimal( blist ) :
  res = []
  for i in range(0,len(blist)/Gene.bits_size):
    res.append(decimal(blist[i*Gene.bits_size:(i+1)*Gene.bits_size]))
  return res

def decimal_to_bin(  dlist ) :
  res = []
  for i in dlist:
    res = res + binary(i)
  return res

def minmax( population ) :
  minimum = maximum = population[0]
  for gene in population :
    if( gene.fitness < minimum.fitness ) :
      minimum = gene
    elif( gene.fitness > maximum.fitness ) :
      maximum = gene
  return( minimum, maximum )

def average( population ) :
  res = 0
  for gene in population :
    res = res + gene.fitness
  return int(res/len(population))

def genetic( populationSize, keepRate, mutationRate, maxIterations) :
  # averages =[]
  # bests = []
  # worsts = []
  Gene.keepRate = keepRate
  Gene.mutationRate = mutationRate
  count = 0
  new_populationSz = int(populationSize * Gene.keepRate) + int(populationSize * Gene.keepRate)%2
  population = []
  fillPopulation(population, populationSize)
  updateFitness(population)
  sortPopulation( population )
  # print population
  # print "Initial : " + str(population)
  finished = False
  cross_point = random.randint(0,Gene.board_size -1)
  while finished == False:
    count = count + 1
    cross_point = (cross_point+1)%Gene.board_size
    population = population[0 : new_populationSz ]
    # for i in range( 0,int(new_populationSz *  )) :
    while len(population) < populationSize :
      gene1, gene2 = select(population)
      gene1, gene2 = gene1.crossover(gene2,cross_point)
      population.append(gene1)
      population.append(gene2)
    for gene in population :
      if random.randint(0,100) < ( 100 * Gene.mutationRate ) :
        gene.mutate()
    #fillPopulation(population,populationSize)
    updateFitness(population)
    if len(population) != populationSize :
      print("Invalid population size! Found: {}, Expected: {}" .format( len(population) , populationSize ))
    sortPopulation( population )
    # worsts.append(population[-1].fitness)
    best = population[0]
    # bests.append(best.fitness)
    # averages.append(average(population))
    # print "Step %02d" % (count,) + ", Best: " + str(28-best.fitness) + ", Average: " + str(average)
    if( best.fitness  == Gene.max_fitness or count >= maxIterations) :
      finished = True
    # try:
    #   import matplotlib.pyplot as plt
    #   plt.plot(averages)
    #   plt.plot(bests)
    #   plt.plot(worsts)
    #   plt.show()
    # except ImportError:
    #   error = 1
  return(count,collisions(best.data))

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



