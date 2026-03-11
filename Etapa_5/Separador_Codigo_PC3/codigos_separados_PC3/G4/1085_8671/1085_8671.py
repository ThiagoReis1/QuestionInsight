n1 = float(input("n: "))
n2 = float(input("n: "))
n3 = float(input("n: "))
n4 = float(input("n: "))
n5 = float(input("n: "))

media = (n1 + n2 + n3  + n4 + n5) / 5
print(round(media, 2))
if media >= 6:

	print("Aprovacao")
else:

	print("Reprovacao")
