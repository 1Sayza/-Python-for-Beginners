numero = int(input("digite um numero para testar se é um numero de kaprekar"))
quadrado = str(numero**2)
i=0
primL,segL=[],[]
while i<len(quadrado):
    if i<(len(quadrado)//2):
        primL.append(quadrado[i])
    elif i>((len(quadrado)//2)-1):
        segL.append(quadrado[i])
    i+=1
prim = int("".join(primL))
seg = int("".join(segL))
kaprekar = prim+seg
if kaprekar == numero:
    print(f"o numero {numero} é um numero de kaprekar pois o quadrado dele é {quadrado}, em que se divide em {prim} e {seg} e {prim}+{seg}={kaprekar}")
else:
    print(f"o numero {numero} não é um numero de kaprekar pois o quadrado dele é {quadrado}, em que se divide em {prim} e {seg} e {prim}+{seg}={kaprekar}")