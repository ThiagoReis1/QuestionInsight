q= float(input("quantidades de horas:"))
h= 20
v=50
v2=70

if(q <= h):
	t= (q*v)
else:
	t= h*v + (q-h)*v2
	
print (round(t,2))