a = float(input("Quantidade de combustivel comum:"))

# Aditivo#
b = 10.50
c = 14.00
d = 18.60
e = 24.5

if a < 17:
	print (round((a + b), 2))
elif a > 17.5 and a < 35:
	print (round((a + c),2))
elif a>35 and a<50:
	print (a + d)
else:
	print (a + e)