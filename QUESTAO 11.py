numero = input("digite um numero para testar se é de kaprekar")
numeroInicial = numero
i=0
while (i<7):
  numeroCresc = sorted(str(numero))
  while len(numeroCresc)<4:
    numeroCresc.insert(0,'0')
  numeroDecr = sorted(numeroCresc,reverse=True)
  n1 = int("".join(numeroCresc))
  n2 = int("".join(numeroDecr))
  
  if n1<n2:
    numero=n2-n1
    print(numeroDecr," ",numeroCresc, " ", numero)
  else:
    numero=n1-n2
    print(numeroCresc," ",numeroDecr, " ", numero)
  i+=1
  if numero==6174:
    print(f"{numeroInicial} convergiu a Kaprekar em {i} conversões")
    break
if numero!=6174:
  print(f"{numeroInicial} Não convergiu a Kaprekar em {i} conversões")
    