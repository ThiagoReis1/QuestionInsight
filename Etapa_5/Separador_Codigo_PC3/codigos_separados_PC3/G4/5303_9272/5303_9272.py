x = int(input("quantidade de massa incicial em gramas: "))
a = 0

while x >= 0.5:
	x = x - (x * 0.1)
	a = a + 1
print(round(a))