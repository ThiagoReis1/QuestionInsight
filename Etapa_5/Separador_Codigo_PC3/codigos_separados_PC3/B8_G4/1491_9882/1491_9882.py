p = float(input("digite:"))
if (0>=p<=5000):
	v = p*0.03+20.0
elif (5001>=p<=6000):
	v = p*0.04+25.0
elif (6001>=p<=7000):
	v = p*0.05+30
elif (p>7000):
	v = p*0.05+35
	
print(round(v, 2))