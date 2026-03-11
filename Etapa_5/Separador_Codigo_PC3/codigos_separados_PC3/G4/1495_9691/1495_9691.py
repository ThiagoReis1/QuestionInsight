x = int(input("insira a area: "))


if (x >= 0) and (x <= 10000):
	v = x*6.00+100.00
elif (x >= 10000) and (x <= 20000):
	v = x*5.50 + 150.00
elif (x >= 20000) and (x <= 30000):
	v = x*5.00+200.00
elif (x >= 30000) and (x <= x ):
	v = x*4.50 + 250.00
else: 
	v = "nao existe"
print(round(v,2))