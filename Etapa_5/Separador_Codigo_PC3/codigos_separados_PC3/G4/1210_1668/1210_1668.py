from numpy import * 
vet_lancamento = array(eval(input("Quais sao as distancia: ")))
r = 74.08
i = 0 
k = 0 
while(i < size(vet_lancamento)):
	if(vet_lancamento[i] < r):
		k = k + 1
	i = i + 1 
print(r)
print(k)