from numpy import*
vet = array(eval(input()))
infracao = 0

for i in range(size(vet)):
	x = ((100*vet[i])/vet[0])
	if(x>120 and x<150):
		infracao = infracao + 1
		print(i)
	
print(infracao)