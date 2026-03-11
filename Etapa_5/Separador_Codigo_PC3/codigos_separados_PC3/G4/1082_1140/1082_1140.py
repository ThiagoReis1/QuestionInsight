var1 = float(input("nota 1: "))
var2 = float(input("nota 2: "))
var3 = float(input("nota 3: "))
var4 = float(input("nota 4: "))
var5 = float(input("nota 5: "))

media = (var1 + var2 + var3 + var4 + var5)/5



if (media >= 5.0):
	print(round(media,1))
	print("Aprovado")
else: 
	print(round(media,1))
	print("Reprovado")