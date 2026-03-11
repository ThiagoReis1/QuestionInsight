nascimento = int(input("ano de nascimento: "))
pais = input("idade minima para dirigir (B) para Brasil, e (E) para Estados unidos: ").upper()

if pais == "B" and nascimento <= 2002:
	idade = (2023 - nascimento ) - 21
	print("sim")
	print(idade)
	
elif pais == "E" and nascimento <= 2005:
	idade = (2023 - nascimento) - 18
	print("sim")
	print(idade)

elif pais == "B" and nascimento >= 2002:
	idade = (2023 - nascimento) - 21
	print("nao")
	print(idade * (- 1))
	
elif pais != "B" or pais != "E":
	print("invalido")
	

	

