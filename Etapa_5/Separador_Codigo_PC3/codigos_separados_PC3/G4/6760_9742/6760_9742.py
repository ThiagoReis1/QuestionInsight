p = int(input("P: "))

m1 = 3.25+30
m2 = 4.5+30
m3 = 6.0+30

if p>10:
	print(round(m3,2))
elif p==10:
	print(round(m2,2))
else:
	print(round(m1,2))