from numpy import*
vet = array(eval(input("quant par de alunos: ")))

ap = 0

for i in range (0,size(vet)):
	if(vet[i])%2==0:
		ap = ap + 1
print(ap)

vet2 = zeros(ap, dtype = int)

j = 0

for i in range (size(vet)):
	if(vet[i]%2==0):
		vet2[j] = i
		j = j + 1
print(vet2)

	
	
	
