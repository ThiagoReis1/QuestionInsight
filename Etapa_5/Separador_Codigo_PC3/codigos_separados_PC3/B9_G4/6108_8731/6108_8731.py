a= float(input("Quantidadde de combustuvel: "))
if a<=17.5:
	c= a+1.5
	print(c)
elif a>17.5 and a<=35:
	c= a+2.3
	print(c)
elif a>35 and a<50:
	c= a+3.3
else: 
	c= a+4.7
	print(c)