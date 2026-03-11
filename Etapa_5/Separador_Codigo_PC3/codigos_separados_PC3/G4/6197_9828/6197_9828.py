aa = 1.6
ta = 0.02
a = float(input("A: "))
t = float(input("T: "))
c = 0

while a < aa:
	a = a + t
	aa = aa + ta
	c = c + 1
	
print(c)