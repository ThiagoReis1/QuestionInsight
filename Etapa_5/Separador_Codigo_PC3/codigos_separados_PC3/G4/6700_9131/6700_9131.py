#diaria do equipamento
e = 50
#taxa de manutencao
t = 30
#solucao
d = int(input("dias: "))
y = e*d + t
total = y + y*18/100
print(round(total, 1))
