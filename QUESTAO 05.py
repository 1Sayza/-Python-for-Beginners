import random
elementos = []
listadesvio = []
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,99))
    elementos.append(qtnumeros)
    media = sum(elementos)/len(elementos)
    j = 0
    while j  < len(elementos):
      listadesvio.append((int(elementos[i])-media)**2)
      j += 1
  variancia = sum(listadesvio)/n
  desviopadrao = variancia**(1/2)
  listacrescente = sorted(elementos)
  if len(listacrescente) % 2 == 0:
    mediana = (int(listacrescente[int(len(listacrescente))//2])+int(listacrescente[int(len(listacrescente)//2)-1]))/2
  else:
    mediana=listacrescente[int(len(listacrescente))//2]
  print("Lista original gerada:\n\n{} \n".format(elementos))
  print("A lista crescente: \n\n{} \n ".format(listacrescente))
  print("A média dos valores da lista é {}.\n ".format(media))
  print("A mediana dos valores dos elementos da lista é {}.\n".format(mediana))
  print("O resultado da variância dos elementos é %.2f. \n" %variancia)
  print("O resultado do desvio padrão dos elementos é %.2f." %desviopadrao)
else:
  print("Coloque uma quantidade positiva!")