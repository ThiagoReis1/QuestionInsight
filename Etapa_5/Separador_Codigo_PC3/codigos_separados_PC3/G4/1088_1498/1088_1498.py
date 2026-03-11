p1 = float(input("digite nota 1: "))
p2 = float(input("digite nota 2: "))
p3 = float(input("digite nota 3: "))
p4 = float(input("digite nota 4: "))
p5 = float(input("digite nota 5: "))
media = (p1 + p2 + p3 + p4 + p5) / 5
print(round(media, 2))
if(media >= 7):
	print("Aprovacao")
else:
	print("Reprovacao")
