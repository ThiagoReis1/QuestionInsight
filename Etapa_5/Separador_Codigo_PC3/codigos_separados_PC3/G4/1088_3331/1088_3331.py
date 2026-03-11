v1= float(input("digite a sua nota: "))
v2= float(input("digite a sua nota: "))
v3= float(input("digite a sua nota: "))
v4= float(input("digite a sua nota: "))
v5= float(input("digite a sua nota: "))

media= (v1 + v2 + v3 + v4 + v5) / 5

if (media >= 7.0):
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao por nota")