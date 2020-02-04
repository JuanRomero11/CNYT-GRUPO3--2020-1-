from sys import stdin
import unittest
import laboratorio1
class Testlaboratorio(unittest.TestCase):
    def testSuma(self):
        self.assertEqual(laboratorio1.suma((5,7), (2,3)), (7,10))
        
    def testDeberiaErrarSuma(self):
        self.assertFalse(laboratorio1.suma((5,7), (2,1))==(7,10))
        
    def testResta(self):
        self.assertEqual(laboratorio1.resta((4,7), (8,3)), (-4,4))
        
    def testDeberiaErrarResta(self):
        self.assertFalse(laboratorio1.resta((4,7), (2,1))==(-4,4))
        
    def testMultiplicacion(self):
        self.assertEqual(laboratorio1.multiplicacion((1,2), (2,3)), (-4,7))

    def testDeberiaErrarMultiplicacion(self):
        self.assertFalse(laboratorio1.multiplicacion((1,2), (2,3))==(-4,8))
        
    def testDivision(self):
        self.assertEqual(laboratorio1.division((1,2), (2,3)), (0.6153846153846154,0.07692307692307693))
        
    def testDeberiaErrarDivision(self):
        self.assertFalse(laboratorio1.division((1,2), (2,3))==(0.65538461538464,0.176923076923076))
        
    def testModulo(self):
        self.assertEqual(laboratorio1.modulo((2,4)),4.47213595499958)
        
    def testDeberiaErrarModulo(self):
        self.assertFalse(laboratorio1.modulo((2,4))==(0.6553848464,0.176923076923076))
        
    def testConjugado(self):
        self.assertEqual(laboratorio1.conjugado((3,80)),(3,-80))
        
    def testPolar(self):
        self.assertEqual(laboratorio1.polar((3,80)),(80.05623023850174,1.533313890103235))
        
    def testSumaVectoresComplejo(self):
        self.assertEqual(laboratorio1.sumaVectoresComplejo([(6,-4),(7,3),(4,-8),(0,-3)],[(16,3),(0,-7),(6,0),(0,-4)]),[(22, -1), (7, -4), (10, -8), (0, -7)])

    def testInversaDeUnVector(self):
        self.assertEqual(laboratorio1.InversaDeUnVector([(2,6)]),[(-2, -6)])
        
    def testEscalarPorVector(self):
        self.assertEqual(laboratorio1.EscalarPorVector((2,6),[(2,5),(4,2)]),[(-26, 22), (-4, 28)])
        
    def testSumaMatrices(self):
        matrizUno,matrizDos=[[(2,6),(-1,3)],[(3,9),(2,-2)]],[[(1,4),(4,7)],[(1,1),(0,5)]]
        self.assertEqual([[(3, 10), (3, 10)], [(4, 10), (2, 3)]],laboratorio1.sumaMatrices(matrizUno,matrizDos))

    def testInversaMatriz(self):
        self.assertEqual([[(0.2, -0.4), (0.25, -0.25)], [(0.17, -0.17), (0.1, -0.1)]],laboratorio1.inversaMatrizImaginaria([[(-0.2,0.4),(-0.25,0.25)],[(-0.17,0.17),(-0.1,0.1)]]))
     
    def testComplejoPorMatriz(self):
        self.assertEqual([[(0,13),(-4,32)],[(22,32),(28,10)]],laboratorio1.complejoPorMatriz((-2,3),[[(3,-2),(8,-4)],[(4,-10),(-2,-8)]]))

    def testMatrizTranspuesta(self):
        self.assertEqual([[(4,5), (0,0),(-1,0)], [(1,0),(6, -2),(0,-1)]],laboratorio1.matrizTranspuesta([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))
      
    def testMatrizConjugada(self):
        self.assertEqual([[(4,-5), (1,0)], [(0,0),(6,2)],[(-1,0),(0,1)]],laboratorio1.matrizConjugada([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]]))    
    

    #   Faltan pruebas de las funciones productoVectoresImaginarios, matrizAdjunta,productoMatricesImaginarias,accionMatrizSobreVector, distanciaMatrices,hermitiana

    def testProductoTensor(self):
        oo=[[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
        h=[[(1/(2**0.5),0)],[(1/(2**0.5),0)],[(1/(2**0.5),0)],[(-1/(2**0.5),0)]]
        x=[[(0,0),(1,0)],[(1,0),(0,0)]]
      










    

if __name__ == "__main__":
    unittest.main()
