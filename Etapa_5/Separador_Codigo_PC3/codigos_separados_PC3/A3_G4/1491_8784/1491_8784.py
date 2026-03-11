peso = int(input("insira um numero real:"))
tarifa = 0.03
taxa = 20
i = 0
v = 0
if peso >= 0 and peso <= 5000:
		v = peso*0.03+20
if peso >= 5001 and peso <= 6000:
		v = peso*0.04+25
if peso >= 6001 and peso <= 7000:
		v = peso*0.05+30
if peso >= 7000 and peso > 7000:
	   v = peso*0.06+35
print(round(v,2))
