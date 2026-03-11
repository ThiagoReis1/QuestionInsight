num = int(input())
pais = input("('B') brasil, ('R') russia: ").upper()
idade =2023 - num

if pais == "B" and idade >=18:
	print("sim")
	dif = idade - 18
	print(dif)
elif pais == "B" and idade <18: 
	print("nao")
	dif = 18 - idade
	print(dif)
	
elif pais == "R" and idade >=21:	
	print("sim")
	dif = idade - 21
	print(dif)
elif pais == "R" and idade < 21:
	print("nao")
	dif = 21 - idade
	print(dif)
else:
	print("invalido")

	