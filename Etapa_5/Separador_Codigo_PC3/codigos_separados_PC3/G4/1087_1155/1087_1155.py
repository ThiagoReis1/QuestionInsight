p1= float(input("digite nota 1"))
p2= float(input("digite nota 2"))
p3= float(input("digite nota 3"))
p4= float(input("digite nota 4"))
media=round((p1 + p2 + p3 + p4)/4,2)
print(media)
if(media>=7):
	print("Aprovado")
else:
	print("Reprovado")
