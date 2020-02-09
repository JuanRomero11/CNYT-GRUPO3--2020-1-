# Library of complex numbers
In this repository you can find and use the following operations:

- Sum of complex numbers

- Product of complex numbers

- Subtraction of complex numbers

- Division of complex numbers

- Complex numbers module

- Conjugate of complex numbers

- Conversion between polar and Cartesian representations

- phase of a complex number.

- Adding complex vectors.

- Inverse (additive) of a complex vector.

- Multiplication of a scalar by a complex vector.

- Adding complex matrices.

- Reverse (additive) of a complex matrix.

- Multiplication of a scalar by a complex matrix.

- Transpose of a matrix / vector

- Conjugate of a matrix / vector

- Attach (dagger) of a matrix / vector

- Product of two matrices (of compatible sizes)

- Function to calculate the "action" of a matrix on a vector.

- Internal product of two vectors

- Standard of a vector

- Distance between two vectors

- Check if a matrix is unitary

- Check if a matrix is Hermitian

- Tensioning product of two matrices / vectors

# Installation
If a version greater than or equal to 3.5 of the Python program is not installed yet, the respective installation will have to be done.
In this space you can find the version and the aforementioned program https://www.python.org/downloads/.

# How does it work
Each function has its respective documentation with which it can be guided to give adequate use to each method implemented to live one or more tuples which will give a representation of a number, whether complex or not.

# Running the tests
In the .py file called laboratory1 there are the different corresponding methods where the logic that was used to develop the operation can be evidenced.

```
from sys import stdin
    import math
def multiplicacion (a, b):
    return (a [0] * b [0] -a [1] * b [1], a [0] * b [1] + a [1] * b [0])
```

and its respective test in the testing file with the name of the corresponding function in the laboratorio1.py

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
# Lincese
The license can be evidenced in [LICENSE](LICENSE)

# Author
### _JUAN GUILLERMO ROMERO_
