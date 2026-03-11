x = float(input("nota 1"))
y = float(input("nota 2"))
z = float(input("nota 3"))
w = float(input("nota 4"))
g = float(input("nota 5"))
media = (round(((x + y + z + w + g) /5),2))
if(media >=6.0): 
	print("Aprovado")
	print(round(media),1)
else
	print("Reprovado")
	print(round(media),1)