import math
lb = float(input("Lado B: "))
lc = float(input("Lado C: "))
ang = math.radians(float(input("Angulo: ")))

la = math.sqrt((lb ** 2) + (lc ** 2) - 2 * lb * lc * math.cos(ang))
print(round(la, 2))