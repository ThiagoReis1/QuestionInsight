av1 = float(input("nota 1: "))
av2 = float(input("nota 2: "))
av3 = float(input("nota 3: "))
av4 = float(input("nota 4: "))

media_aritmetica = (av1 + av2 + av3 + av4) /4

print(round(media_aritmetica, 2))

if (media_aritmetica>=5.0):
	mensagem=("Aprovacao")
else:
	mensagem=("Reprovacao")
print(mensagem)