a = float(input("valor de vendas: "))

if (a<=1000):
	b = a*0.05
else:
	d = a-1000
	b = (1000*0.05)+(d*0.10)
	
print(round(b,2))
    