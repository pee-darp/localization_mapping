from my_lib import *

p = init_world(5)
world = ['g','r','r','g','g']
Z = 'g'
pHit = 0.6
pMiss = 0.2

def sense(p,Z):
    q = []
    for i in range(0,len(p)):
        if (Z==world[i]):
            q.append(p[i]*pHit)
        else:
            q.append(p[i]*pMiss)
        
    return (div_list(q,sum(q)))

print (sense(p,Z))
