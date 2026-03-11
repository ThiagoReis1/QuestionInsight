ano = int(input("Qual o ano de nascimento do candidato? "))
pais = input("Qual o pais que o candidato esta, Brasil(B) ou Estados Unudos(E)? ").upper()
anoat = 2023
anobe = 2023 - ano
if((anobe <= 2005) and (pais == "B")):
	print("sim")
	print(anobe - 18)
elif((anobe > 2005) and (pais == "B")):
	print("nao")
	print(anobe-18)
elif((anobe <= 2007) and (pais == "E")):
	print("sim")
	print(anobe - 16)
elif((anobe > 2007) and (pais == "E")):
	print("nao")
	print(16 - (anobe - 2023))
elif((pais != "B") or (pais != "E")):
	print("invalido")
	