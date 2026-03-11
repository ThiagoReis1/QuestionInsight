mg = float(input("Massa do peixe grande: "))
vg = float(input("Velocidade do peixe gande: "))
mp = float(input("Massa do peixe pequeno: "))
vp = float(input("Velocidade do peixe pequeno: "))

vf = ((mg*vg)-(mp*vp))/(mg+mp)
print(vf)