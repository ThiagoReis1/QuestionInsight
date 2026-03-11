mg = float(input("Insira a massa de g: "))
vg = float(input("Insira a velocidade de g: "))
mp = float(input("Insira a massa de p: "))
vp = float(input("Insira a velocidade de p: "))

vf = (mg*vg - mp*vp)/(mg+mp)
print(vf)