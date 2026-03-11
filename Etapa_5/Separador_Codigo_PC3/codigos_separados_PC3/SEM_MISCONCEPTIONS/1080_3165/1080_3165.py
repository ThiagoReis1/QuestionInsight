prova_1 = float(input("Nota da primeira prova: "))
prova_2 = float(input("Nota da segunda prova: "))
prova_3 = float(input("Nota da terceira prova: "))

media_aritmetica = (prova_1 + prova_2 + prova_3)/3
print(round(media_aritmetica, 1))

if(media_aritmetica>=5.0):
	print("Aprovado")
else:
	print("Reprovado")