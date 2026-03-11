#peixe grande
Mg = float(input("Mg: "))
Vg = float(input("Vg: "))

#peixe pequeno
Mp = float(input("Mp: "))
Vp = float(input("Vp: "))

#velocidade Vf
Vf = ((Mg * Vg) - (Mp * Vp))/(Mg + Mp)

print(Vf)