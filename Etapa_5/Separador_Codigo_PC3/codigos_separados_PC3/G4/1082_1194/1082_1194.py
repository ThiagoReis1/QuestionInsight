a = float(input("Nota da prova a: "))
b = float(input("Nota da prova b: "))
c = float(input("Nota da prova c: "))
d = float(input("Nota da prova d: "))
e = float(input("Nota da prova e: "))

media_aritmetica = (a + b + c + d + e) / 5

print(round(media_aritmetica, 1))

if (media_aritmetica >= 5.0):
	print("Aprovado")
else:
	print("Reprovado")