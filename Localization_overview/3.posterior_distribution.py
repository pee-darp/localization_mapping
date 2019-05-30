from my_lib import *

p=[]
n = 5

for i in range(0,n):
    p.append(1.0/n)
    
pHit = 0.6
pMiss = 0.2

for i in range(0,n):
    if (i==2 or i==3):
        p[i] = pHit*p[i]
    else:
        p[i] = pMiss*p[i]

total = sum(p)

p = div_list(p,total)

print (p)




