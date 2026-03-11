p= float(input("preco de custo:"))
p1= (100/100)
p2= (50/100)
p3= (40/100)
p4= (30/100)
if (p > 0) and (p <= 50):
	t= (p + (p*p1))
elif (p > 50) and (p <= 100):
	t=(p + (p*p2))
elif (p > 100) and (p <= 500):
	t= (p + (p*p3))
else:
	t= (p + (p*p4))

print(round(t,2))