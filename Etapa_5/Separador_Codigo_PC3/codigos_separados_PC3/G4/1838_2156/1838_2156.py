#Variaveis

R1 = float(input("valor de R1"))

R2 = float(input("valor de R2"))

R3 = float(input("valor de R3"))

#Resistencia Equivalente

Req = (R1 * R2 * R3) / ((R1 * R2) + (R2 * R3) + (R1 * R3))

print(Req)