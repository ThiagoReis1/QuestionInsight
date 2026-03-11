p1=float(input("digite p1:"))
p2=float(input("digite p2: "))
p3=float(input("digite p3: "))

media= (p1 + p2 + p3)/3 
print(round(media, 1))
if(media >= 7.0):
	print("Aprovado")
else:
	print("Reprovado")