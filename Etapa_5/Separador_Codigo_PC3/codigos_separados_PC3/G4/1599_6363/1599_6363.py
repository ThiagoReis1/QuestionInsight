from numpy import*

vet = array(eval(input("produtos: ")))
v = 80.0
i = 0
j = 0
while(vet[i] > v ):
	j = j + (vet[i] * 15)/100 
	i = i + 1
s = sum(vet)
print(round(s, 2))

