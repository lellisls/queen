def board(vec):
    print ("\n".join( str(i+1)  + ' ~> ' + 'O ' * (i) + 'X ' + 'O ' * (n-i-1) for i in vec) + "\n")

def collisions(vec):
  val = 0
  for i in range(0,len(vec)):
    for j in range(1,len(vec)):
      if i != j :
        if vec[i] == vec[j] :    
          val = val + 1
        if abs(j-i) == abs(vec[j] - vec[i]) :
          val = val + 1
          
          
  return val
    
n = 8
count = 0
cols = range(n)

    print str(collisions( vec )) + "  collisions."
    if collisions(vec) == 0:
        #print vec
      board ( vec )
      break
      
print str(count) + " trys."
