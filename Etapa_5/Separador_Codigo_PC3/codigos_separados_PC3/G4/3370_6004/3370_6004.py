uni = input("unidade que a medida esta: ").upper()
v_m = float(input("valor da medida: "))

p = 0.393701

if (uni == "C"):
	mc = (p * v_m)
else:
	mc = (v_m / p)
	
print(round(mc, 2))
