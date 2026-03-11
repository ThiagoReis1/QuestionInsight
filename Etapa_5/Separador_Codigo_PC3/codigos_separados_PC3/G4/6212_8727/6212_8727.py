nums = int(input("numeros saudaveis:"))
cont = 0
while nums != -1:
	if nums >= 25 and nums <= 85:
		cont = cont + 1
	nums = int(input("numeros saudaveis:"))	
print(cont)		
	
	