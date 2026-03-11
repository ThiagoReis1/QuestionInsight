v=float(input("premio: "))
s=float(input("saquer: "))
j=float(input("juros: "))

if(v>0 and s>0 and j>0 ):
	bol=v
	mes=0
	while(bol<=(1.2*v)):
		
		bol=bol+bol*(j/100)
		
		bol=round(bol-s,2)
		mes=mes+1
	print(mes)
	
	
	
	
	
else:
	print("Dados incorretos")