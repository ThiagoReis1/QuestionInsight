from numpy import*


vet = array(eval(input()))
i = 0
j = 0
saq = 0


for elemento in vet:
	if(elemento <= 50):
		saq = saq + 1

vat = zeros(saq, dtype=int)

for elemento in vet:
	if(elemento <= 50):
		vat[j] = i
		j = j +1
	i = i +1
		
	
print(saq)
	
print(vat)