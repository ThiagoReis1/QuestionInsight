p1=float(input("valor da p1"))
p2=float(input("valor da p2"))
p3=float(input("valor da p3"))
p4=float(input("valor da p4"))
p5=float(input("valor da p5"))

media=(p1+p2+p3+p4+p5)/5

print(round(media,2))

if(media>=6):
	print("Aprovado")
else:
	print("Reprovado")
