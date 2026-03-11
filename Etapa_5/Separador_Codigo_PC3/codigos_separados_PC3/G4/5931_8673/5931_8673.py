qm =  float(input("insira o valor de qm: "))

v = (45.0 + 0.97 * qm)
taxa = v + (v * 0.42)

print(round(taxa, 2))