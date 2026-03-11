
p = float(input(""))
r = int(input(""))
if r == 1 :
	f = 10
else:
	if r == 2 :
		f = 8
	else:
		if r == 3 :
			f = 0
		else :
			f = 2
v = (p - (p * 0.40)) + (p * (f / 100))
print(round(v, 2))




