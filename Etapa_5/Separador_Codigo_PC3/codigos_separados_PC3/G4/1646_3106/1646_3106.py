from numpy import*
vet = array(eval(input("Saques: ")))

menor = 0

for i in vet:
	if(i <= 50):
		menor = menor + 1
	
z = zeros(menor,dtype=int)

a=0
b=0

for w in vet:
	if(w <= 50):
		z[a] = b
		a = a + 1
	b = b + 1
	
print(menor)
print(z)