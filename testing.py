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

    def testMatrizAdjunta(self):
        res=[[(1, 2), (5, 6)], [(-3, -4), (-7, -8)]]
        rescod=laboratorio1.matrizAdjunta([[(1,-2),(-3,4)],[(5,-6),(-7,8)]])
        self.assertEqual(res,rescod)

    def testProductroMatrices(self):
        self.assertEqual([[(9,6), (5,-4)], [(10, 30), (0,0)],[(4,1),(0,1)]],laboratorio1.productoMatricesImaginarias([[(4,5),(1,0)],[(0,0),(6,-2)],[(-1,0),(0,-1)]],[[(1,-1),(0,-1)],[(0,5),(0,0)]]))

    def testAccionMatrizVector(self):
        self.assertEqual([(9, -3), (-15, 0)],laboratorio1.accionMatrizSobreVector([(-3,1),(5,0)],[[(2,0),(3,-1)],[(3,1),(-1,0)]]))

    def testNormaMatriz(self):
        self.assertEqual(16.492,laboratorio1.normaMatriz([[(4,5),(6,7)],[(8,9),(0,-1)]]))

    def testDistanciaMatrices(self):
        self.assertEqual(12.923,laboratorio1.distanciaMatrices([[(2,6),(-1,3)],[(3,9),(2,-2)]],[[(1,4),(4,7)],[(1,1),(0,5)]]))

    def testUnitaria(self):
        self.assertEqual(True,laboratorio1.unitaria([[(1,0),(0,0)],[(0,0),(1,0)]]))

    def testHermitiana(self):
        self.assertEqual(True,laboratorio1.hermitiana([[(1,0),(0,0)],[(0,0),(1,0)]]))

    def tesProductoTensor(self):
        m=[[(1,1),(0,0)],[(1,0),(0,1)]]
        m1=[[(-1,2),(-2,-2),(0,2)],[(2,3),(3,1),(2,2)],[(-2,1),(1,-1),(2,1)]]
        self.assertEqual([[(-3, 1), (0, -4), (-2, 2), (0, 0), (0, 0), (0, 0)], [(-1, 5), (2, 4), (0, 4), (0, 0), (0, 0), (0, 0)], [(-3, -1), (2, 0), (1, 3), (0, 0), (0, 0), (0, 0)], [(-1, 2), (-2, -2), (0, 2), (-2, -1), (2, -2), (-2, 0)], [(2, 3), (3, 1), (2, 2), (-3, 2), (-1, 3), (-2, 2)], [(-2, 1), (1, -1), (2, 1), (-1, -2), (1, 1), (-1, 2)]],laboratorio1.productoTensor(m,m1))   

if __name__ == "__main__":
    unittest.main()
