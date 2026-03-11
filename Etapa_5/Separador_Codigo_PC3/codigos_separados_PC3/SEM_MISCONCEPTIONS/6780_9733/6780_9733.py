idade = int(input("Digite:"))
ct = input("Digite:")
idade2 = 2023-idade

if (ct.upper()) == 'B' and idade2 >= 21:
	print("sim")
	print(idade2-21)

elif (ct.upper()) == 'C' and idade2 >= 24:
	print("sim")
	print(idade2-24)
	
elif (ct.upper()) == 'B' and idade2 < 21:
	print("nao")
	print(21-idade2)
	
elif (ct.upper()) == 'C' and idade2 < 24:
	print("nao")
	print(24-idade2)
	
else:
	print("invalido")
	
	
