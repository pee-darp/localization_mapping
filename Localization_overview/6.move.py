p = [0,1,0,3,0]

def move(p,U):
    n = len(p)
    U = U%n
    q = []
    for i in range(0,n):
        q.append(p[(i+n-U)%n])
    return q
print (move(p,2))

def inexact_move(p,U,pExact,pOvershoot,pUndershoot):
    n = len(p)
    U = U%n
    q = []
    for i in range(0,n):
        q.append(pExact*(p[(i+n-U)%n])+ pOvershoot*(p[(i+n-U-1)%n]) + pUndershoot*(p[(i+n-U+1)%n]))
    return q
print (inexact_move(p,2,0.8,0.1,0.1))
