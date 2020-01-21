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
def fase(a):
    return math.atan(a[1]/a[0])

def sumaVectoresComplejo(vector1,vector2):
    vectorFinal=[]
    for i in range(len(vector1)):
        vectorFinal.append(suma(vector1[i],vector2[i]))
    return vectorFinal

def InversaDeUnVector(vectorInicial):
    vectorFinal=[]
    for i in vectorInicial:
        vectorFinal+=[(-i[0],-i[1])]
    return vectorFinal
#donde se operara un complejo(num) y vector(lis) el cual retornara un vector final(lis)
def EscalarPorVector(num,lis):
    final=[]
    for i in range(len(lis)):final+=[multiplicacion(num,lis[i])]
    return final

def sumaMatrices(matInicial,matInicial2):
    lista=[[None]*len(matInicial) for i in range(len(matInicial2))]
    for i in range(len(matInicial)):
        for j in range(len(matInicial2)):lista[i][j]=suma(matInicial[i][j],matInicial2[i][j])
    return lista




    
