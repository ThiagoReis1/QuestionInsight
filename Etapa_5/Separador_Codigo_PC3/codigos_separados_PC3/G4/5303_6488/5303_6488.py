m = int(input("Digita ai: "))

a = 0

while (m > 0.5):
	m = m - (10/100) * m
	a = a + 1
	
print(round(a, 2))