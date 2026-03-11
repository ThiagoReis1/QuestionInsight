z = int(input("Quantos zumbis invadiram?: "))
h = int(input("Quantos habitantes existem na vila?: "))
x = int(input("Pessoas transformadas em zumbi por dia: "))
y = int(input("zumbis mortos por exterminadores por dia: "))
D = 0

while(h > 0):
	z = z*x
	z = z-y
	h = h - z
	D = D +1
print(D)