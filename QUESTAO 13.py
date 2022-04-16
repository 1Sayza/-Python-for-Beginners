gabarito = ["a","b","c","d","e","a","b","c","d","e"]
matriz = []
provas = []
for i in range(0,2):
  linhamatriz  = []
  matriz = []
  for j in range(0,11):
      if j == 0:
        opcoes = input("Digite o nome do aluno: ")
        opcoes=opcoes.lower()
      else:
        opcoes = input("Digite o gabarito do aluno: ")
        opcoes=opcoes.lower()
      linhamatriz.append(opcoes)
  matriz.append(linhamatriz)
  corretas = 0
  l = 0
  while l < 10:
    if str(linhamatriz[l+1]) == str(gabarito[l]):
      corretas+=1
    l +=1
  matriz.append(corretas)
  provas.append(matriz)
b = 0
while b < len(provas):

  print(f"A aluno(a) {provas[b][0][0]} obteve a nota {provas[b][1]}" ,end="")
  c = 0
  print(" e as opções marcas foram:")
  while c < len(provas[b][0])-1:
    print(f" {provas[b][0][c+1]}")
    c+=1
  if int(provas[b][1]) == len(provas[b][0])-1:
    print(" Aluno(a) Gabaritou.")
  else:
    print("")
  b+=1