x=int(input("Determine o X: "))
n3= x%10
sobra3=x//10
n2= sobra3%10
n1= sobra3//10


if ( x== (n1**3)+(n2**3)+(n3**3)):
	print(x,"atende a propriedade")
else:	
	final=(n1**3)+(n2**3)+(n3**3)	
	print(final)



