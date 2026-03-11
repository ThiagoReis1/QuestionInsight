cc = float(input("Quantidade de combustivel comum: "))

if (cc<17.5):
	t = cc + 10.5
	print(round(t,1))
elif (cc>=17.5) and (cc<35):
	t = cc + 14
	print(round(t,1))
elif (cc>=35) and (cc<50):
	t = cc + 18.6
	print(round(t,1))
else:
	t = cc + 24.5
	print(round(t,1))