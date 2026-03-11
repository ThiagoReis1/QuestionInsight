n= int(input("n: "))

par = int(0)
soma = int(0)
while(n!=0):
	
	if(n%2 ==0):
		par = par +1
		
	soma = soma +1
	n= int(input("n: "))	

print(soma)	
print(round(par/soma*100,2))
