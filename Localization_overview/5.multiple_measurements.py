from my_lib import *

p = init_world(5)
w = ['g','r','r','g','g']
Z = ['r','r','r']

for z in range(len(Z)):
    p = sense(w,p,Z[z],0.6,0.2)

print(p)
