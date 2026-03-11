mg = float(input("Massa do peixe 1?"))

vg = float(input("Velocidade do peixe 1?"))

mp = float(input("Massa do peixe 2?"))

vp = float(input("Velocidade do peixe 2?"))

vf = (mg*vg - mp*vp) / (mg+mp)
print(vf)