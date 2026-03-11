n = int(input("Termos:"))
y = 3
i = 1
x = 1
e = 0
s = (1 ** 2)/(1 + 3)

while(n >= 1):
	if(i % 2 == 0):
		s =  s - e
	else:
		s =  s + e
	i = i + 1
	x = x + 1
	y = y + 2
	e = (x ** 2)/(1 + y)
print(round(s, 7))
	