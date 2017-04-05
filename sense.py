#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    sumQ = sum(q)
    normQ = [x/sumQ for x in q]
    return normQ
for k in range(len(measurements)):
    p = sense(p, measurements[k])

print(p)

def sum(*arg1):
  sumTotal = 0
  for i in arg1:
    sumTotal += i
  return sumTotal

def sum(one, two)

def sum(one, two, three):

