from math import sqrt

def racines(a,b,c):
    delta = b**2-4*a*c
    if delta == 0:
        x0 = (-1*b)/(2*a)
        print("Delta = 0","\nx0 =",x0)
    elif delta > 0:
        x1 = (-1*b-sqrt(delta))/(2*a)
        x2 = (-1*b+sqrt(delta))/(2*a)
        print("Delta =",delta,"\nx1 =",x1,"\nx2 =",x2)
    else:
        print("Delta =",delta,"\nPas de racines")
        
