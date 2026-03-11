vi = float(input("Digite o valor do ingresso: "))
ing = int(input("Digite a quantidade de ingressos: "))
vd = (vi*20)/100
vp = vi-vd
vt = vp * ing
print(round(vt, 2))