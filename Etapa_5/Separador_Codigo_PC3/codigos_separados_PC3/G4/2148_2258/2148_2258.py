from numpy import* 

vet = array(eval(input("Vetor: "))) 

p = 0
c = 0

for x in range(size(vet)):
	p = p + vet[x]
	if(vet[x] >= 5):
		c = c + 1
print(p)
print(c)