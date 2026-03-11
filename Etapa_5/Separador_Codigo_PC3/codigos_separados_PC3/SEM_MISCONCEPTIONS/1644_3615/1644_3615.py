from numpy import *

entrada = array(eval(input()))

qtd_repro = 0
#vet = zeros(4, dtype=int)

for i in range(size(entrada)):
	if entrada[i] < 5.0:
		qtd_repro+=1
print(qtd_repro)
vet = zeros(qtd_repro,dtype=int)
t = 0
for j in range(size(entrada)):
	if entrada[j] < 5.0:
		vet[t] = j
		t+=1
print(vet)