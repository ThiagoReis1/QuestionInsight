p = float(input("Digite o valor: "))
cod = int(input("Codigo da regiao: "))
if(cod==1):
	total = p-(p*0.40)+(p*10/100)
	print(round(total,2))
if(cod==2):
	total = p-(p*0.40)+(p*8/100)
	print(round(total,2))
if(cod==3):
	total = p-(p*0.40)
	print(round(total,2))
if(cod==4):
	total = p-(p*0.40)+(p*2/100)
	print(round(total,2))