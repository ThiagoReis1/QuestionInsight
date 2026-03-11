c = float(input("digite um numero: "))

if (3000.0 <= c < 3400.0):
	t = c * 0.8
	print(round(t,1))
elif(3400.0 <= c < 3900.0):
	t = c * 1.3
	print(round(t,1))
elif(3900.0 <= c < 4100.0):
	t = c * 2.1
	print(round(t,1))
else:
	t = c * 3.0
	print(round(t,1))