# ENTRADAS mg vg mp e vp
mg = float(input("Massa do peixe grande: "))
vg = float(input("Velocidade do peixe grande: "))
mp = float(input("Massa do peixe pequeno: "))
vp = float(input("Velocidade do peixe pequeno: "))

# velocidade final do peixe grande
vf = ((mg*vg) - (mp*vp)) / (mg + mp)

print(vf)

