num = int(input("digite:"))
pais = input("digite:").upper()

idade = 2023 - num

if ((pais != "B" and pais != "I")) or (idade < 0):
	print("invalido")

elif (pais == "B") and (idade >= 18):
	ano = num + 18
	anos = 2023 - ano
	print("sim")
	print(anos)
	
elif (pais == "B") and (idade < 18):
	anos2 = 18 - idade
	print("nao")
	print(anos2)
	
elif (pais == "I") and (idade > 17):
	ano2 = num + 17
	anos3 = 2023 - ano2
	print("sim")
	print(anos3)
	
else:
	(pais == "I") and (idade < 17)
	anos4 = 17 - idade
	print("nao")
	print(anos4)