p1=float(input("digite nota 1:"))
p2=float(input("digite nota 2:"))
p3=float(input("digite nota 3:"))
media= round((p1+p2+p3)/3,1)
print(media)
if float(media>=5.0):
	print("Aprovado")
else:
	print("Reprovado")