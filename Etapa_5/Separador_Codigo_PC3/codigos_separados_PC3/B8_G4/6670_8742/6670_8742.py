from numpy import*
vet = array(eval(input("precos: ")))
soma = zeros(size(vet),dtype=float)
m = 0

for i in range(size(vet)):
	if vet[i] > 20:
		soma[i] = vet[i]
		m += 1
	elif vet[i] < 20:
		soma[i] = 0
if sum(soma)== 0:
	print(0.0)
else:	
	somaFoda = sum(soma)/m
	print(round(somaFoda, 2))