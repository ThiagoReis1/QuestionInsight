x = float(input("insira um numero que pertenca ao dominio: "))

if (x >= -100 and x < 0):
	f = -1*1/x
	print(round( f,4))
elif (x > 0 and x <= 100):
	f = 1/x
	print(round(f,4))
else:
	print("entrada invalida")