import random
elementos = []
i = 0
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,99))
    elementos.append(qtnumeros)
  print("Lista original gerada:\n {}".format(elementos))
  print("Lista em ordem decrescente: \n {} " .format(sorted(elementos, reverse = True)))
else:
  print("Coloque uma quantidade positiva!")