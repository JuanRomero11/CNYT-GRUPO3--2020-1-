from sys import stdin
import math
def suma(a,b):
    return (a[0]+b[0],a[1]+b[1])
def resta(a,b):
    return (a[0]-b[0],a[1]-b[1])
def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def division(a,b):
    return ((a[0]*b[0]+a[1]*b[1])/((b[0]**2)+(b[1]**2)),((a[1]*b[0]-a[0]*b[1])/((b[0]**2)+(b[1]**2))))
def modulo(a):
    return (a[0]**2+a[1]**2)**(1/2)
def conjugado(a):
    return (a[0],-a[1])
def polar(a):
    return (modulo(a), math.atan(a[1]/a[0]))


