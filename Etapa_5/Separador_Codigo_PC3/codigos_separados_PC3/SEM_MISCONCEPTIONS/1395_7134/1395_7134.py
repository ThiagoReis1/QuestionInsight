vend = float(input("valor de venda:"))

if vend <= 1000:
	total = (vend*5)/100
else:
	exc = vend - 1000
	total = ((1000*5)/100)+((exc*10)/100)
print(round(total, 2))