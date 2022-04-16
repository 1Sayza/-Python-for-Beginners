import random
import statistics as st
elementos = []
n = int(input("Diga quantos elementos a lista possuirá: "))
if n > 0:
  for i in range(0,n):
    qtnumeros = (random.randint(0,99))
    elementos.append(qtnumeros)
    media = st.mean(elementos)
    mediana = st.median(elementos)
    variancia = st.pvariance(elementos)
    desviopadrao = st.pstdev(elementos)
  print("Lista original gerada:\n\n{} \n".format(elementos))
  print("A média dos valores da lista é {}.\n ".format(media))
  print("A mediana dos valores dos elementos da lista é {}.\n".format(mediana))
  print("O resultado da variância dos elementos é %.2f. \n" %variancia)
  print("O resultado do desvio padrão dos elementos é %.2f." %desviopadrao)
else:
  print("Coloque uma quantidade positiva")