v= float(input("valor do consumo: "))
if (v<300):
	t = v*0.10 + v
else:
	t = v*0.06 + v
print(round(t,2))