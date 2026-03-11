#provas de Meroveu

av1 = float(input(" nota1:"))
av2 = float(input(" nota2:"))
av3 = float(input(" nota3:"))

media = (av1 + av2 + av3)/3

if(media >= 5):
	print(round(media,1))
	print("Aprovado")
else:
	print(round(media,1))
	print("Reprovado")