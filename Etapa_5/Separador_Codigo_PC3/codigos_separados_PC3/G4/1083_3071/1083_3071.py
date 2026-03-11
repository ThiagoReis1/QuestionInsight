a = float(input("Digite: "))
b = float(input("Digite: "))
c = float(input("Digite: "))
m = (a + b + c) / 3
if (m >= 6.0):
	print(round(m, 2))
	print( "Aprovacao" )
else:
	print(round(m, 2))
	print( "Reprovacao" )