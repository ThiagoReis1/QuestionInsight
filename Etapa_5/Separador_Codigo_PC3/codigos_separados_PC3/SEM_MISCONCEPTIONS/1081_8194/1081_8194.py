not1 = float(input("nota 1: "))
not2 = float(input("nota 2: "))
not3 = float(input("nota 3: "))
not4 = float(input("nota 4: "))

media = not1 + not2 + not3 + not4
media2 = media/4

if(media2 >= 5):
	print(round(media2, 2))
	print("Aprovacao")
else:
	print(round(media2, 2))
	print("Reprovacao")