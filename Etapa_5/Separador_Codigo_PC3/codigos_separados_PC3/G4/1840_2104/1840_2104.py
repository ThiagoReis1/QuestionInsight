n = int(input("numero de mols:"))
v = float(input("volume:"))
t = float(input("temperatura:"))
k = (273.1+t)

p = (n * 0.082057 * k)/v
print(p)
