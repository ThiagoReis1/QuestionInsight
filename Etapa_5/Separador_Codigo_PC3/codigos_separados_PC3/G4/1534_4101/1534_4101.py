x = float(input("Numero real: "))
k = int(input("Numero de termos: "))

a = 0 
i = 1
s = 0

while (k > a):
	s = s + ((x**i)/i)
	a = a + 1
	i = i + 2
print(round(s, 7))