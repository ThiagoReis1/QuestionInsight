bme = float(input("Comprimento da base menor:"))
bma = float(input("Comprimento da base maior:"))
h = float(input("Altura:"))
cf = float(input("Custo do fertilizante por m2:"))

A = ((bme+bma)*h)/2
print(round(A*cf,2))