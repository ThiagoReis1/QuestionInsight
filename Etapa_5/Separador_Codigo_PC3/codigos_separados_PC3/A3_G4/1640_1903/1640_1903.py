from numpy import*

vet = array(eval(input("vet: ")))


nimp = 0
j = 0

for i in range(size(vet)):
	if(vet[i]%2 != 0):
		nimp += 1

nvet = zeros(nimp, dtype = int)
nimp = 0
for i in range(size(vet)):
	if(vet[i]%2 != 0):
		nvet[nimp] = i
		nimp += 1
		
print(nimp)
print(nvet)
