a = float(input(""))
if 3000 <= a < 3400:
	c = a*0.8
	print(c)
elif a>=3400 and a<3900:
	c = a*1.3
	print(c)
elif a>=3900 and a<4100:
	c = a*2.1
	print(c)
else : 
	c = a*3
	print(c)