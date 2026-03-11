p = float(input(""))
d = float(input(""))
cod = input("")

pr = ((p * 25 ) + (d * 0.10))

if (cod == "1"):
	tt = pr * (1 + (17/100))
elif (cod == "2"):
	tt = pr * (1 + (17.5/100))
elif (cod == "3"):
	tt = pr * (1 + (18/100))
else:
	tt = pr * (1 + (20/100))
print(round(tt,2))