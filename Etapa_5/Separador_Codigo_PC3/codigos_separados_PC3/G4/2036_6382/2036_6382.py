c=input("cor da casa: ")

c=c.upper()
x=0

while(c!="S"):
	
	if(c=="PRETA"):
		x = x + 1
		
	c=input("cor da casa: ")
	c=c.upper()
	
print(x)
