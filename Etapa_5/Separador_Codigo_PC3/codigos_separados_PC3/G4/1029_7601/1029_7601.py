c = float(input("Insira o consumo de chamadas em minutos: "))

v = (c * 0.28) + 23
vt = v * (31/100)
vt_2 = v + vt

print(round(vt_2,2))