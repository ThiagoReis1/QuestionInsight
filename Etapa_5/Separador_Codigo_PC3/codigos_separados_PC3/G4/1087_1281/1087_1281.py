#Karen Hanna Schoaba - 21600523
#Avaliacao 02 - Ex01
#30/06/2016

x1=float(input("Nota 1"))
x2=float(input("Nota 2"))
x3=float(input("Nota 3"))
x4=float(input("Nota 4"))
media=(x1+x2+x3+x4)/4

print(round(media, 2))
if media >= 7:
	print("Aprovado")
else:
	print("Reprovado")	