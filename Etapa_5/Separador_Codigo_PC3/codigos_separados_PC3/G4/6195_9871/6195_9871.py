from numpy import*
b = int(input())
t = int(input())
h = 0
dobro = b * 2
while b < dobro:
	h += 1
	b += b * (t/100)
print(h)

