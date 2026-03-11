ql = float(input("digite quantos litros foram abastecidos: "))

t1 = ql*(2.86) + 50
t2 = 0.34*t1
t = t1 + t2
print(round(t, 2))