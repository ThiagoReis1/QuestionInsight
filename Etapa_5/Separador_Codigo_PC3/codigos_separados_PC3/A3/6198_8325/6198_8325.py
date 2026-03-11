altura_luna = 1.65
taxa_luna = 0.02

altura=float(input("altura da pessoa: "))
taxa=float(input("taxa de crescimento: "))


c=taxa

while(altura>altura_luna):
	if(altura<altura_luna):
		c=c+altura
		
	
print(c)	
