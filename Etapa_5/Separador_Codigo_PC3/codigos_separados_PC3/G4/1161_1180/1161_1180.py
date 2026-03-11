Z = int(input("Informe Horda Z:"))
H = int(input("Informe nro de Habitantes H:"))
X = int(input("Informe capacidade de transformar X:"))
Y = int(input("Informe a capacidade de extermínio Y:"))
n = 0
while (H > 0):
	H = H - (Z * X)
	Z = Z + (Z * X)
	Z = Z - Y
	n = n + 1
	
print(n)