from numpy import*

saque = array(eval(input("saques:")))
lista = 0

for i in range(size(saque)):
	if saque[i] <= 50:
		lista += 1
		
ind = zeros(lista, dtype=int)
print(lista)
f = 0
for i in range(size(saque)):
	if saque[i] <= 50:
		ind[f]= i
		f += 1
print(ind)