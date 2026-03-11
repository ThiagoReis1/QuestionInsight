mg = float(input("Massa peixe grande: "))
vg = float(input("Velocidade peixe grande: "))
mp = float(input("Massa peixe pequeno: "))
vp = float(input("Velocidade peixe pequeno: "))
velocidade = float(mg*vg - mp*vp) / (mg + mp)

print(velocidade)