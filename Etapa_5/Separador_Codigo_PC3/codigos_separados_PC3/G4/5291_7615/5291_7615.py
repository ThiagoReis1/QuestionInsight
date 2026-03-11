r= input("digite a resposta:").upper()
cont= 0
c= 0
while (r != "S"):
	cont= cont + 1
	if (r == "SIM"):
		c= c + 1
	p= (c/cont)*100
	r=input("digite a resposta:").upper()
print(round(cont,2))
print(round(p,2))