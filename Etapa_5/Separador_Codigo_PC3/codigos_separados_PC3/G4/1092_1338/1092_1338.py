n1 = int(input("Insira um numero: "))

if(n1%2!=0):
	a= n1//100
	b= a/a
	c= b**3
	
	
	a1=n1%11
	b2= a1**3
	
	
	a3=n1%10
	b3= a3**3
	
	somafinal= (c+b2+b3)
	print(somafinal)
	
else:
	
	print(n1,"atende a propriedade")