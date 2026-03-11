#peso do saco em g
#quantidade de racao diaria em g
p = float(input("peso do saco da racao: "))
qd = float(input("quantidade diaria de racao" ))

qs = p - qd * 7
print(round(qs, 2))

#quantidade de racao em (g) apos uma semana
# round(x,n)