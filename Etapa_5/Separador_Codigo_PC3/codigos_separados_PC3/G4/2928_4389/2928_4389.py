mg = float(input("Informe a massa do peixe grande:\n"))
vg = float(input("Informe a velocidade do peixe grande:\n"))
mp = float(input("Inforne a massa do peixe pequeno:\n"))
vp = float(input("Informe a velocidade do peixe pequeno:\n"))

vf = (mg*vg - mp*vp)/(mg + mp)
print(vf)

