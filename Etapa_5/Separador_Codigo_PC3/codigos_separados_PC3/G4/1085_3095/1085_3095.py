p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())

mp = (p1 + p2 + p3 + p4 + p5 ) / 5
print(round(mp, 2))

if (mp < 6):
	print("Reprovacao")
else:
	print("Aprovacao")