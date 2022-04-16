import random
elementos = []
qt1 = qt2 = qt3 = qt4 = 0
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,99))
    elementos.append(qtnumeros)
    if qtnumeros <= 24:
      qt1 +=1
    elif 25<= qtnumeros <= 49:
      qt2 +=2
    elif 50 <= qtnumeros <= 74:
      qt3 +=3
    elif 75 <= qtnumeros <= 99:
      qt4 +=4
  print(elementos)
  print("A quantidade de vezes que os números entre 0 e 24 aparece é {}.".format(qt1))
  print("A quantidade de vezes que os números entre 25 e 49 aparece é {}.".format(qt2))
  print("A quantidade de vezes que os números entre 50 e 74 aparece é {}.".format(qt3))
  print("A quantidade de vezes que os números entre 75 e 99 aparece é {}.".format(qt4))
else:
  print("Coloque uma quantidade positiva!")