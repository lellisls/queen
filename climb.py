import math
import random
from common import *

def sucessors(vec) :
	suc = []
	for i in range(0,len(vec)):
		for j in range(0,len(vec)):
			if vec[i] != j :
				aux = list(vec)
				aux[i] = j
				suc.append(aux)
	return suc

def best(suc) :
	res = suc[0]
	minimum = 1000000
	for s in suc :
		c = collisions(s)
		if c == minimum :
			# Flip a coin
			if( random.getrandbits(1) == 1) :
				res = s
		elif c < minimum :
			res = s
			minimum = c

	return { "vec" : res , "val" : minimum }

n = 8
count = 0
#finished = False
#while finished == False :
vec = generate(n)
# print "Initial : " + str(vec)
while collisions(vec) != 0:
	count = count + 1
	s = sucessors(vec)
	b = best(s)
	if b["val"] >= collisions(vec) :
		break
	else :
		vec = b["vec"]
if collisions(vec)==0 :
	finished = True
print "Final  :  " + str(vec) + "\n"
board(vec)
print str(count) + " iterations."
print str(collisions(vec)) + " collision(s)."
