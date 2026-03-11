vi = int(input(" "))
bd = int(input(" "))
r = int(input(" "))

c = vi
minutos = 0

while (c > 1000):
	c = (c + bd - r)
	minutos = minutos + 1
print(minutos)