nome = input("nome do aminoácido: ")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if(nome == "histidina"):
	peso1 = (c*6) + (h*10) + (n*3) + (o*2)
	print(round(peso1,2))

else:	
	peso2 = (c*5) + (h*10) + n + (o*2)
	print(round(peso2,2))