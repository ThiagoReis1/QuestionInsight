bac = float(input("Digite o numero inicial de bacterias:"))
hrs = float(input("Digite a quantidade de horas:"))
if(bac <= 0): 
	print("quantidade invalida")
else:
	if (hrs<=0):
		print("Hora invalida")
	cont=bac
	temp=0
	while(temp < hrs):
	  # cont = cont + 2 / 100 * cont
		cont = int( cont + 2 /100 * cont)
		temp = temp + 1	
print(cont)
	