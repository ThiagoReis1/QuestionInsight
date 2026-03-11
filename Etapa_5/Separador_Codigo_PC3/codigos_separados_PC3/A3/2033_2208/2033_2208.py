result=input("Digite o nome da sua unidade academica(ICE, FT, ICOMP ou FCA): ")
x=0
n=0
while(result.upper()!="S"):
	if(result.upper()=="ICOMP"):
		x=x+1	
	result=input("Digite o nome da sua unidade academica(ICE, FT, ICOMP ou FCA): ")
print(x)