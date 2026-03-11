p1 = float(input("Digite o valor da nota: "))
p2 = float(input("Digite o valor da nota: "))
p3 = float(input("Digite o valor da nota: "))
p4 = float(input("Digite o valor da nota: "))
p5 = float(input("Digite o valor da nota: "))

media = ((p1)+(p2)+(p3)+(p4)+(p5)) / 5
print(round(media, 2))

if(media>=7):
	print("Aprovacao")
else:
	print("Reprovacao")
	