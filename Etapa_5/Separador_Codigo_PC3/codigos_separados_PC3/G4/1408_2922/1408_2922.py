a = input ("Katana ou Sabre: ")
d = int (input ("destreza: "))
d1 = int (input ("D1: "))
d2 = int (input ("D2: "))
s = d1 + d2
k = 2 * s + d
b = s + 2 * d
if (a.upper() == "KATANA"):
	print (k)
else:
	print (b)