from numpy import*

vet = array(eval(input("valores")))

i = 0
v = 0
a = 0

while(i < size(vet)): 
	if vet[i] >90:
		v = vet[i] - 6.50
		a = a + 6.50
	i = i + 1
print(round(sum(vet)-a, 2))