nascimento = int(input("insira: "))
pais = input("Digite (B) para Brasil e (E) para EUA: "). upper()
idade = 2023 - nascimento

if idade >= 18 and pais == "B" or idade >= 16 and pais == "E":
	print("sim")
	print(idade - 16)

elif idade < 18 and pais == "B" or idade < 16 and pais == "E":
	print("nao")
	print(idade - 18)
 
	
else: 
	print("invalido")