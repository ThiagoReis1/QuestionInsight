a=int(input(""))

if  a>0 and a<10:
	c=a*2.0+20
	print(round(c,2))
elif a>=10 and a<20:
	c=a*2.5+20
	print(round(c,2))
elif a>=20 and a<40:
	c=a*2.75+20
	print(round(c,2))
elif a>=40:
	c=a*3.0+20
	print(round(c,2))
else:
	print("dados invalidos ")
	