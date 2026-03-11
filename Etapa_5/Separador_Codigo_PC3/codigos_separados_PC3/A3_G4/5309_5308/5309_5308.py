from math import*

x = float(input("x: "))

k = int(input("k: "))

ac = 0

serie = 0

while (ac < k):
	ac = ac + 1
	impar = 2 * k + 1
	s = x / factorial(impar)
	se = x + s
print(round(se, 8))