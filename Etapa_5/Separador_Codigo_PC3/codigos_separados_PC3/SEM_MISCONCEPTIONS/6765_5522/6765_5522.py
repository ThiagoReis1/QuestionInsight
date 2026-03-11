n = int(input())
p = input().upper()
idade = 2023-n
if p == "B":
	if idade >=18:	
		print("sim")	
		print(18-idade)	
	else:	
		print("nao")	
		print(18-idade)
elif p == "R":	
	if idade >=21:	
		print("sim")	
		print(idade-21)	
	else:	
		print("nao")	
		print(idade-21)
else:	
	print("invalido")