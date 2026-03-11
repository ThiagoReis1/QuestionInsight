a = int(input("terreno:"))
if (a<=10000):
	v=a*6.00+100
elif (10000<a<=20000):
	v=a*5.5+150
elif (20000<a<=30000):
	v=a*5+200
else:
	v=a*4.5+250
print(v)