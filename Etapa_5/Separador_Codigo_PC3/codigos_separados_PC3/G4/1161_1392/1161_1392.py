z = int(input("quantidade de zumbis: "))
h = int(input("população: "))
x = int(input("pessoas transformadas: "))
y = int(input("zumbis mortos: "))

t = 1

while(z < h):
	z = z*x - y
	t = t + 1
print(t)