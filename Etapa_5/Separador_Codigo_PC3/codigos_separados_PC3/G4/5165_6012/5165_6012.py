#em gramas
p = float(input("peso do saco: "))
q = float(input("quantidade de racao: "))
# calculo de quanto restara no saco
consumo = (q * 6)
s = p - consumo
print(round(s, 4))