p1 = float(input("prva 1: "))
p2 = float(input("prva 2: "))
p3 = float(input("prva 3: "))
p4 = float(input("prva 4: "))

media = (p1 + p2 + p3 + p4)/4

if(media>=5.0):
	print(round(media, 2))
	print("Aprovacao")
else:
	print(round(media, 2))
	print("Reprovacao")