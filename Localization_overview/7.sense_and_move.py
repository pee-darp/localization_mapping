from my_lib import *

p = init_world(5)
world = ['g','r','r','g','g']
U = [1,1,2,-3,1,1,1,1]
Z = ['r','g','g','r','g','g','g','r']

for i in range(len(U)):
    p = inexact_move(p,U[i],0.8,0.1,0.1)
    p = sense(world,p,Z[i],0.6,0.2)

print(p)
