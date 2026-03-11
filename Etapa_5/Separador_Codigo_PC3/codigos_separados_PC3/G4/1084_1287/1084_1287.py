x = float(input("digite a nota 1: "))
y = float(input("digite a nota 2: ")) 
u = float(input("digite a nota 3: "))
z = float(input("digite a nota 4: "))
media = (x+y+u+z)/4
if (media >= 6 ):
	print(round(media , 1))
	print("Aprovado")
else:
	print(round(media , 1))
	print("Reprovado")