nasc = int(input("digite o ano de nascimento: "))
pais = input("digite B ou C: ").upper()
ano = 2023
brasil = 21
china = 24

consulta = ano - nasc
if(pais == "B" and consulta >= brasil):
	y = int(consulta - brasil)
	print("sim")
	print(y)
elif(pais == "B" and consulta < brasil):
	y = int(brasil - consulta)
	print("nao")
	print(y)
elif(pais == "C" and consulta >= china):
	y = int(consulta - china)
	print("sim")
	print(y)
elif(pais == "C" and consulta < china):
	y = int(china - consulta)
	print("nao")
	print(y)
else:
	print("invalido")