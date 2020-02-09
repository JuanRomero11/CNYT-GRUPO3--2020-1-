# Libreria de numeros complejos
En este repositorio se podra encontrar y utilizar las siguientes operaciones:

- Suma de numeros complejos

- Producto de numeros complejos

- Resta de numeros complejos

- División de numeros complejos

- Módulo de numeros complejos

- Conjugado de numeros complejos

- Conversión entre representaciones polar y cartesiano

- fase de un número complejo.

- Adición de vectores complejos.

- Inverso (aditivo) de un vector complejo.

- Multiplicación de un escalar por un vector complejo.

- Adición de matrices complejas.

- Inversa (aditiva) de una matriz compleja.

- Multiplicación de un escalar por una matriz compleja.

- Transpuesta de una matriz/vector

- Conjugada de una matriz/vector

- Adjunta (daga) de una matriz/vector

- Producto de dos matrices (de tamaños compatibles)

- Función para calcular la "acción" de una matriz sobre un vector.

- Producto interno de dos vectores

- Norma de un vector

- Distancia entre dos vectores

- Revisar si una matriz es unitaria

- Revisar si una matriz es Hermitiana

- Producto tensor de dos matrices/vectores

## Instalacion
Si aun no esta instalado una version mayor o igual 3.5 del programa Python, se tendra que ehacer la respectiva instalacion.
En este espacio se podra encontrar la version y el programa antes mencionado https://www.python.org/downloads/.

## Como funciona
Cada funcion tiene su respectiva documentacion con la cual se podra guiar para dar un adecuado uso a cada metodo implementado para resivir una o varias tuplas las cuales daran una representacion de un numero ya sea complejo o no.

# Ejecutando las pruebas
En el archivo .py llamado laboratorio1 se encuentran los diferentes metodos correspondientes donde se puede evidenciar la logica que se utilizo para desarrollar la operacion.
```
		from sys import stdin
    import math
		def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
		
```
y su respectiva prueba en el archivo testing con el nombre a la funcion que corresponde en el archivo de laboratorio1.py
```
		from sys import stdin
    import unittest
    import laboratorio1
    class Testlaboratorio(unittest.TestCase):
        def testMultiplicacion(self):
            self.assertEqual(laboratorio1.multiplicacion((1,2), (2,3)), (-4,7))

        def testDeberiaErrarMultiplicacion(self):
            self.assertFalse(laboratorio1.multiplicacion((1,2), (2,3))==(-4,8))
```
## Lincese 
La licencia se púede evidenciar en [LICENSE](LICENSE) 
## Autor 


### _JUAN GUILLERMO ROMERO_
