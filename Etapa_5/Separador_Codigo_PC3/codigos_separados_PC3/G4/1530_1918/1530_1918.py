a = int(input(""))
b = int(input(""))
c = float(input(""))
d = float(input(""))
i = 0
while( a + b <= 80000):
	a = a + (a*c)/100
	b = b + (b*d)/100
	i = i + 1
print(i)