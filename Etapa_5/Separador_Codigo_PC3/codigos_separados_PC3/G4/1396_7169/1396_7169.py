v = float(input("valor consumido? "))
if v<=300:
	a = (10/100)*v+v
else:
	a = (6/100)*v+v
print(round(a, 2))
	