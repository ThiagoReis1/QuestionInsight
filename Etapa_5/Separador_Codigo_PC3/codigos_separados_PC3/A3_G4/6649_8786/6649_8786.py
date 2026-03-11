from numpy import*
notas = input("digite as notas: ")
contador_e = 0
i = 0

p1 = 3 * notas[0]
p2 = 2 * notas[1]
p3 = 4 * notas[2]
p4 = 1 * notas[3]
p5 = 3 * notas[-1]

i += 1

mp = (p1 + p2 + p3 + p4 + p5) / (1 + 2 + 3 + 4 + 3)
print(round(mp, 2))