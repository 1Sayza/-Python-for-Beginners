import random
import numpy as np
matriz = []
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
    for i in range(0,n):
        linhamatriz = []
        for j in range(0,n):
            qtnumero = random.randint(0,9)
            linhamatriz.append(qtnumero)
        matriz.append(linhamatriz)
    det = np.linalg.det(matriz)
    print("A determinante da matriz é: %.2f. \n" %det)
    print(" {} \n".format(matriz))
else:
    print("A quantidade elementos deve ser um inteiro positivo!")



            
    

  
