n = float(input("escreva o número de mols: " ))
v = float(input("volume: "))
j = float(input("temperatura: "))
r = 0.082057


t = float(j + 273.1)

f = (n * r * t)/v

print(f)
