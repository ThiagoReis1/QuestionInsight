from numpy import*
v = array(eval(input("digite o valor: ")))

s = 0
for i in range(size(v)):
	if(v[i]<=50):
		s = s + 1
print(s)
j = 0
cont = 0
vet = zeros(s, dtype=int)
for j in range(size(v)):
	if(v[j]<=50):
		vet[cont]= vet[cont] + 1
print(vet)