import random
elementos = []
i = 0
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,9))
    elementos.append(qtnumeros)
  print(elementos)
  print("A quantidade de vezes que o número 0 aparece é {}.".format(elementos.count(0)))
  print("A quantidade de vezes que o número 1 aparece é {}.".format(elementos.count(1)))
  print("A quantidade de vezes que o número 2 aparece é {}.".format(elementos.count(2)))
  print("A quantidade de vezes que o número 3 aparece é {}.".format(elementos.count(3)))
  print("A quantidade de vezes que o número 4 aparece é {}.".format(elementos.count(4)))
  print("A quantidade de vezes que o número 5 aparece é {}.".format(elementos.count(5)))
  print("A quantidade de vezes que o número 6 aparece é {}.".format(elementos.count(6)))
  print("A quantidade de vezes que o número 7 aparece é {}.".format(elementos.count(7)))
  print("A quantidade de vezes que o número 8 aparece é {}.".format(elementos.count(8)))
  print("A quantidade de vezes que o número 9 aparece é {}.".format(elementos.count(9))) 
else:
  print("Coloque uma quantidade positiva!")