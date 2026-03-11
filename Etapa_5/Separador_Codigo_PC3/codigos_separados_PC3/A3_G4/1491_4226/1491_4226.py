p = int(input("Peso (g) > "))
v = 0

if p <= 5000:
	v = p*0.03 + 20
elif p >= 5001 and p < 6000:
	v = p*0.04 + 25
elif p >= 6001 and p < 7000:
	v = p*0.05 + 30
else:
	v = p*0.06 +35
round(v,2)
print(v)