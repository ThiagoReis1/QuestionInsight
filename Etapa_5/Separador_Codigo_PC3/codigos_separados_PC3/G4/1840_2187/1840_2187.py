n = float(input("Número de mols: "))
V = float(input("Volume: "))
T = float(input("Temperatura em graus Celcius: ")) + 273.1

R = 0.082057

p = (n * R * T) / V

print(p)