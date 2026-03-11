num = int(input("Entre com o tempo de permanencia: "))
fixo = 5.0 

if (num < 2):
	cst =  (fixo + 1.25)
	
elif (num == 2):
	cst =  (fixo + 2.25)
	
elif (num > 2):
	cst =  (fixo + 3.25)
	
print(round(cst,2))