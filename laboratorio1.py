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

def EscalarPorVector(num,lis):
    final=[]
    for i in range(len(lis)):final+=[multiplicacion(num,lis[i])]
    return final

def sumaMatrices(matInicial,matInicial2):
    lista=[[None]*len(matInicial) for i in range(len(matInicial2))]
    for i in range(len(matInicial)):
        for j in range(len(matInicial2)):lista[i][j]=suma(matInicial[i][j],matInicial2[i][j])
    return lista


def inversaMatrizImaginaria(MatrizInicial):
    matriz = []
    for i in range(0,len(MatrizInicial)):
        matriz.append(InversaDeUnVector(MatrizInicial[i]))
    return matriz

def complejoPorMatriz(c1,MatrizInicial):
    matriz=[]
    for i in range(0,len(MatrizInicial)):
        vector=[]
        for j in range(0,len(MatrizInicial[0])):
            vector.append(multiplicacion(MatrizInicial[i][j],c1))
        matriz.append(vector)
    return matriz


def matrizTranspuesta(matrizInicial):
    matriz=[]
    for i in range(0,len(matrizInicial[0])):
        columna = [x[i] for x in matrizInicial]
        matriz.append(columna)
    return matriz 
        
     
def matrizConjugada(MatrizInicial):
    matriz=[]
    for i in range(0,len(MatrizInicial)):
        vector=[]
        for j in range(0,len(MatrizInicial[0])):
            vector.append((MatrizInicial[i][j][0],MatrizInicial[i][j][1]*-1))
        matriz.append(vector)
    return matriz
''' funcion ayuda '''
def productoVectoresImaginarios(c1,c2):
    ini = (0,0)
    for i in range(le(c1)):
        suma = productoImaginarios(c1[i],c2[i])
        ini = sumaImaginarios(ini,suma)
    return ini

def matrizAdjunta(MatrizInicial):
    matriz=matrizTranspuesta(MatrizInicial)
    matriz=matrizConjugada(matriz)
    return matriz


def productoMatricesImaginarias(MatrizInicial,m2):
    matriz = [[None] * len(m2[0]) for i in range(len(MatrizInicial))]
    for i in range(len(MatrizInicial)):
        for j in range(len(m2[0])):
            columna = [row[j] for row in m2]
            matriz[i][j] = productoVectoresImaginarios(MatrizInicial[i],columna)
    return matriz

def accionMatrizSobreVector(v1,MatrizInicial):
    v = []
    for i in range(len(MatrizInicial)):    
            v.append(productoVectoresImaginarios(v1,MatrizInicial[i]))
    return v


   


def distanciaMatrices(mat1,mat2):
    mat_fin=[[(0,0)]*len(mat1[0]) for x in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat_fin[i][j]=resta(mat1[i][j],mat2[i][j])
    res=norma_mat(mat_fin)
    return res

# EnConstruccion
##def unitaria(mat):
# EnConstruccion
##def normaMatriz(mat):
def productoTensorialImaginario(matriz1,matriz2):
    matriz = []
    for i in range(len(matriz1)):
        matM = [[]] *len(matriz2)
        for j in range(len(matriz1[i])):
            m3 = complejoPorMatriz(matriz1[i][j],matriz2)
            for k in range(len(matriz2)):
                
                matM[k] = matM[k] + m3[k]
        for k in range(len(matriz2)):
            matriz.append(matM[k])
    return matriz

def hermitiana(mat):
    if mat==mat_adjun(mat):
        return True
    else:
        return False


    

    
