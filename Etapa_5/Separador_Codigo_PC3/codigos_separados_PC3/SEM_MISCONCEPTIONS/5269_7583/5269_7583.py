num = int(input("numero inteiro: ")) 

cont = 0  
cont1 = 0

while(num != 0 ): 
	if(num > 0):
		cont = cont +1 
	cont1 = cont1 + 1
	num = int(input("numero inteiro"))	
print(round(cont,2))
cont = (cont/cont1 * 100) / 3
		
		
		