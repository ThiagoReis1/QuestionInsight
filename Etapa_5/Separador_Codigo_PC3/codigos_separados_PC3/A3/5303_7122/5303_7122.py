massa = int(input(""))


cont = 0
soma = 0

while (massa >= 0.5):
	cont = cont + 1
	massa = massa - (massa*10/100)

print(round(cont,2))
	
	
	