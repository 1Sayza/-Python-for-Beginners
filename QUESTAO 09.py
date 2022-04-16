import random
elementos = []
i = 0
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,1000))
    elementos.append(qtnumeros)
  print(elementos)
  x = int(input("Diga um valor na escala de 0 a 1000: "))
  if x in elementos:
    print("A posição do valor {} na lista se encontra em {}.".format(x,(elementos.index(x))))
  else:
    print("Não existe na lista o valor {}.".format(x))
else:
  print("Coloque uma quantidade positiva!")