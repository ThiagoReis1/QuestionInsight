p=round(float(input('Preco: ')),2)
if p<=50.00:
	c=p+p
	print(round(c,2))
elif (p>50.01 and p<=100.00):
	c=(0.5*p+p)
	print(round(c,2))
elif p>100.01 and p<=500.00:
	c=(0.40*p+p)
	print(round(c,2))
elif p>500.00:
	c=(0.30*p+p)
	print(round(c,2))