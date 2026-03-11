x = float(input())

if x<0 and x>=-4:
	f = (abs(x) ** (1/2))
elif x<=4 and x>=0:
	f = (x ** (1/2))
else:
	print("entrada invalida")

print(round(f, 4))
