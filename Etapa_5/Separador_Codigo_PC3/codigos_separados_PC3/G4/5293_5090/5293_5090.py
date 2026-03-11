x = int(input("numero: "))

cont = 0
soma = 0

while(x!=0) :
	soma = soma +1
	if((x%2==0) ):
		
		cont = cont + 1
		
	x = int(input("n: "))	
	
print(soma)
print(round(((cont/soma)*100),2))