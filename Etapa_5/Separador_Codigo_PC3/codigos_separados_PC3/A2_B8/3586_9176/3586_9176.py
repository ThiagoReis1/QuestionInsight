from numpy import *
pontos = array(eval(input("Digite o vetor de pontos que ele fez: ")))
tam = size(pontos)
i = 0
total = 0
while i < tam:
 if pontos[i] == 1:
  total += 100
 elif pontos[i] == 2:
  total += 60
 elif pontos[i] == 3:
  total += 20
 elif pontos[i] == 4:
  total = total
 i += 1
print(total)