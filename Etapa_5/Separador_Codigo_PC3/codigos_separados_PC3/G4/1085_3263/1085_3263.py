p1 = float(input("nota: "))
p2 = float(input("nota: "))
p3 = float(input("nota: "))
p4 = float(input("nota: "))
p5 = float(input("nota: "))

media = (p1 + p2 + p3 + p4 + p5) / 5

if (media >= 6):
	mensag = ("Aprovacao")
	
else:
	mensag = ("Reprovacao")
	
print(round(media, 2))
print(mensag)