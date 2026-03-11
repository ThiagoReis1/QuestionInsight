a = float(input("Qantidade de combustivel:"))
if a<=17.5:
	c= a+10.5
	print(c)
elif a>17.5 and a<=35:
	c= a+14.0
	print(c)
elif a>35 and a<50:
	c= a+18.6
else:
	c= a+24.5
	print(c)