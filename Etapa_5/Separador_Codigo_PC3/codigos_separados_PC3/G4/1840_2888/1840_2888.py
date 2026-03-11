# Grandezas:
m = float(input("Numero de mols: "))
v = float(input("Volume: "))
t = float(input("Temperatura: "))

# Soma:
temp = t + 273.1

# Valores:
r = 0.082057

# Equaçao:
p = m * r * temp / v

print(p)