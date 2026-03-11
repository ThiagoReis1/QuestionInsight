from numpy import*

v = array(eval(input("Digite os numeros sorteados: ")))
x = zeros(37, dtype=int)
#contar a quantidade de vezes que um numero de 1 a 36 aparece e depois imprimilos em um vetor x em sua respectiva posicao
for i in v:
   x[i] = x[i] + 1



print(x)
