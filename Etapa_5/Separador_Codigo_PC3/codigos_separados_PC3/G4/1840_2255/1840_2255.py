n = float(input("mols: "))
v = float(input("volume: "))
k = float(input("temperatura: "))
r = 0.082057
t = float(k+273.1)
f = (n*r*t)/v
print(f)