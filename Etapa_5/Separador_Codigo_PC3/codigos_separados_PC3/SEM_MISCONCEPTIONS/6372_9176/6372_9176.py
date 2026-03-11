from numpy import *
compras = input("Digite todas as compras que voce fez no spermercado: ").upper().split(",")
vetor = zeros(4, dtype = int)
for i in compras:
 if i == "A":
  vetor[0] += 1
 if i == "B":
  vetor[1] += 1
 if i == "L":
  vetor[2] += 1
 if i == "H":
  vetor[3] += 1
print(vetor)