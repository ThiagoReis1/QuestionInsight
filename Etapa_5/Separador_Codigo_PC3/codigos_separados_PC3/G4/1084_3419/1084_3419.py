av1 = float(input("nota av1"))
av2 = float(input("nota av1"))
av3 = float(input("nota av1"))
av4 = float(input("nota av1"))
media = (av1 + av2 + av3 +av4 ) / 4


if (media <= 6.0):
	print(round(media,1))
	print("Reprovado")
else :
	print(round(media,1))
	print("Aprovado")