from numpy import*
saque = array(eval(input("digite vetor: ")))

i = 0
acu = 0
for i in range(size(saque)):
	if (saque[i] >= 2000):
		acu = acu + 1
		
vetornovo= arange(acu)

print(acu)
contnovo = 0
for i in range(size(saque)):
	if (saque[i] >= 2000):
		vetornovo[contnovo]=  i 
		contnovo = contnovo + 1
	

print(vetornovo)
	
	
	
