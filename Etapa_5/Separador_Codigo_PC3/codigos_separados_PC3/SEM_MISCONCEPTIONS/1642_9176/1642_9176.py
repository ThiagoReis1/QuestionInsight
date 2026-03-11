from numpy import *

alunos = array(eval(input("Digite a quantidade de alunos em cada turma: ")))
qtde = 0

for i in range (size(alunos)):
 if alunos[i] % 5 == 0:
  qtde += 1

vetor = zeros(qtde, dtype = int)
b = 0

for i in range (size(alunos)):
 if alunos[i] % 5 == 0:
  vetor[b] = i
  b += 1

print(qtde)
print(vetor)