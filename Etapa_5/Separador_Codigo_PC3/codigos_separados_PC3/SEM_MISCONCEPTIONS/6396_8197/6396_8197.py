from numpy import *

vet = array(eval(input("Digite a sequencia de numeros: ")))
substituto = zeros(size(vet), dtype=int)

for i in range(vet):
	substituto[] = vet[i] * 2