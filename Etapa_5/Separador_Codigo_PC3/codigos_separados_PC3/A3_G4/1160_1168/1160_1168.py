

H = int(input("num de habitantes: "))
V = int(input("num de vampiros: "))
X = int(input("pessoas transformadas: "))
Y = int(input("vampiros mortos por dia: "))

dia = 0
vamp = 0

while ((V + X) - Y < H):
	dia = dia + 1
	vamp = (V + X) - Y
print(dia)
