cn = float(input("o consumo de chamadas em minutos durante um mes: "))
plano = cn*0.28
vf = 23
vt = plano + vf
vt2 = vt%31
vt3 = vt + vt2
print(vt3)


