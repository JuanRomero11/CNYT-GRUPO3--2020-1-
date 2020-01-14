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

if __name__ == "__main__":
    unittest.main()
