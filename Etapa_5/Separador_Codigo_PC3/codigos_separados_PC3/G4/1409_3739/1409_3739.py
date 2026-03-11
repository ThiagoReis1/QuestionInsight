ataque = input("qa")
d1 = int(input("a"))
d2 = int(input("a"))
d3 = int(input("a"))
d4 = int(input("a"))
s1 = d1+6
s2= d2+6
s3 = d3+6
s4 = d4+6
if (ataque == "espada"):
	m = s1+s2+s3+s4
else:
	m = (d1+d2+d3)*d4
print(m)