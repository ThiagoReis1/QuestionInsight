me = float(input("Minutos excedente: "))
vp = 45 + (0.97 * me)
p =  vp * 42 / 100
r = vp + p
print(round(r,2))