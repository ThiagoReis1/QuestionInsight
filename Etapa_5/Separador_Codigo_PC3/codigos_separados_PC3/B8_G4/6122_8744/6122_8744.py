c = float(input("digite um numero: "))

if (c > 0) and (c < 17.5):
	a = c + 0.8
	print(round(a,1))
elif (c > 0) and (17.5 <=  c < 35.0):
	a = c + 1.3
	print(round(a,1))
elif (c > 0) and (35.0 <= c < 50.0):
	a = c + 2.1
	print(round(a,1))
elif (c > 0) and (50.0 <= c):
	a = c + 3.0
	print(round(a,1))