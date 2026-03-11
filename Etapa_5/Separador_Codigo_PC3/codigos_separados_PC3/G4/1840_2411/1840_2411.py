M = int(input("Numero de mols:"))
V = float(input("volume:"))
Temp = float(input("Temperatura em graus Celsius:"))

R = 0.082057

T = Temp + 273.1

p = (M * R * T)/V

print(p)