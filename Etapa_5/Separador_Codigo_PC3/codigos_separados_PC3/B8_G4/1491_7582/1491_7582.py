from numpy import*
p = float(input("encomenda "))
if p  >= 0 and p <= 5000:
	t = 0.03
	tax = 20
	v = p * t + tax
elif p > 5001 and p <=6000:
	t = 0.04
	tax = 25
	v = p * t + tax
elif p > 6001 and p <= 7000:
	t = 0.05
	tax = 30
	v = p * t + tax
elif p>7000:
	t = 0.06
	tax = 35
	v = p * t +tax
print(v)
	