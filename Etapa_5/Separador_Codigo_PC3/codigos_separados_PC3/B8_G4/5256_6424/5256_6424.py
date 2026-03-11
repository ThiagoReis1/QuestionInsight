a = float(input())
f = float(input())
t = f - a
if 0 < t :
	print("saldo positivo")
elif t == 0:
	print("sem variacao")
elif  t < 0:
	print('saldo negativo')