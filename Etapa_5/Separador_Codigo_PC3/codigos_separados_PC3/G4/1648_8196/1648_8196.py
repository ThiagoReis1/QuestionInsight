from numpy import*
var1 = array(eval(input(": ")))
cont = 0
cont1 = 0
i = 0
for i in range(size(var1)):
	if(var1[i] <70):
		cont = cont + 1
vet = zeros(cont, dtype = int)
for i in range(size(var1)):
	if(var1[i] <70):
		vet[cont1] = i
		cont1 = cont1 + 1
print(cont)
print(vet)
		
		
