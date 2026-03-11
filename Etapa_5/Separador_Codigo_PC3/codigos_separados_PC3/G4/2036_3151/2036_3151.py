cor= input()
z=0
c=cor.upper()
if(c=="PRETA" or c=="VERMELHA" or c== "S"):
	while(c!="S"):
		if(c=="PRETA"):
			z=z+1
		c=input()
		c=c.upper()
		
print(z)