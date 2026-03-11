p = float(input("pressao:"))
n = float(input("mols:"))
t = float(input("temperatura: "))
y = t + 273.15
r = 0.082
print((n * r * y) / p)