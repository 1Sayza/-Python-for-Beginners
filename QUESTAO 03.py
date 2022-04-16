import random
crescente =[]
i = j = 0
menornumero=100
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,99))
    crescente.append(qtnumeros)
  print("Lista original gerada:\n {}".format(crescente))
  while True:
    completo=True
    i=1
    while i-1<len(crescente):
      if i<len(crescente):
        if crescente[i-1]>crescente[i]:
          crescente[i],crescente[i-1]=crescente[i-1],crescente[i] 
          completo=False
      i+=1
    if completo==True:
      break
  print("Lista em ordem crescente: \n {} " .format(crescente))
else:
  print("Coloque uma quantidade positiva!")