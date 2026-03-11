pr1 = float(input())
pr2 = float(input())
pr3 = float(input())

m = (pr1 + pr2 + pr3) / 3
x = round(m, 2)

if(m >= 6.0):
	print(x, "Aprovacao")
else:
	print(x, "Reprovacao")