
import random
import math

def board(vec):
	n = len(vec)
	print ("\n".join( 'O ' * (i) + 'X ' + 'O ' * (n-i-1) for i in vec) + "\n")

def collisions(vec):
	tuples = []
	for i in range(0,len(vec)):
		for j in range(1,len(vec)):
			if i != j :
				if vec[i] == vec[j] or abs(j-i) == abs(vec[j] - vec[i]):
					if i < j :
						tuples.append((i,j))

	return len(tuples)

def generate( n ) :
	# return random.sample(xrange(0,n), n)
	v = []
	for i in range( 0, n ) :
		v.append(random.randint(0,n-1))
	return v

def mean( data ) :
	s = 0
	for i in data :
		s = s + i
	return float(s)/float(len(data))

def std( data, m ) :
	s = 0
	for i in data :
		sub = i - m
		s = sub * sub
	return math.sqrt(s)

