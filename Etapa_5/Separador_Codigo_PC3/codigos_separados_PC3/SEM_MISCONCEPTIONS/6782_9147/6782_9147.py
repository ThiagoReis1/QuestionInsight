nasc = int(input("Insira sua idade: "))
pais = input("Digite (B) para Brasil e (E) para Estados Unidos: ").upper()

idade = 2023 - nasc
if	idade >= 16 and pais == "E":
	print("sim")
	print(idade - 16)
elif	idade >= 18 and pais == "B":
	print("sim")
	print(idade - 18)
elif	idade < 16 and pais == "E":
	print("nao")
	print(16 - idade)
elif	idade < 18 and pais == "B":
	print("nao")
	print(18 - idade)

else:
	print("invalido")