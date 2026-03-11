V=float(input("Informe o valor de de vendas: "))
if (V<=1000.00):
	     c=float(V*(5.00/100.00))
else:
	  c=float((1000.00*(5.00/100.00))+((V-1000.00)*(10.00/100.00)))
	
print(round(c,2))
