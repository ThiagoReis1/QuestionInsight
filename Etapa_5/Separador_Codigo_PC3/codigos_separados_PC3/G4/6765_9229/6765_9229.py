n = int(input(""))
pais = input("B/R? ").upper()

x = 2023-n 

if  pais == "B":
	if x >= 18:  
		print("sim")
		y = 18-(2023-n) 
		print(y)
	else:
		print("nao") 
		y = 18-(2023-n)          
		print(y)
		
elif pais == "R": 
	if x >= 21:
		print("sim")
		y = 21-(2023-n)
		print(y)
	else:
		print("nao")
		y = 21-(2023-n) 
		print(y)
else:
	print("invalido") 