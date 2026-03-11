a = int(input("Insira o Valor: "))
total = 0
facesseis = 0

while(a != -1 and a <= 6):
	total = total + 1
	
	if(a == 6):
		facesseis = facesseis + 1
	
	a = int(input("Insira o Valor: "))	

porcent = (facesseis/total) * 100

print(total)
print(round(porcent, 2))