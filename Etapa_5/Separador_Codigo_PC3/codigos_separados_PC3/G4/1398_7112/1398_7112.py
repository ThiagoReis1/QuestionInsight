Voo = float(input("voo: "))

t = 200

if ( Voo <= t):
	c = (Voo * 100) + 5000
else:
	T = Voo - t
	ti = 200* 100
	c = (T * 90) + 8000 + ti
	
print(round(c,2))