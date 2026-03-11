nasc = int(input("insira o ano de nascimento:"))
pais=input("insira o pais de nascimento").upper()

idade = 2023 - nasc 

if pais == "B":
	if idade >= 18:
		print("sim")
		y=(2023 - nasc) - 18 
		print(y)
	else:
		print("nao")
		y = 18 - (2023 - nasc)
		print(y)
elif pais == "J":
	if idade >= 16:
		print("sim")
		y = (2023 - nasc) - 16
		print(y)
	else: 
		print("nao")
		y = 16 - (2023 - nasc)
		print(y)
else:
	print("invalido")