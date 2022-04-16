elementos = []
i = 0
x = int(input("Diga quantos elementos a lista possuirá: "))
while True:
  n = int(input("Informe um valor: "))
  if n == 0:
    break
  elementos.append(n)
  elementos.sort()
  i +=1
  print(elementos[0:x])