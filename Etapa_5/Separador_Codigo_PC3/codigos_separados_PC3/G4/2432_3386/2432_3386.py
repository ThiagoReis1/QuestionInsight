pa= float(input("Preco da area por m2: "))
ap= int(input("Area privativa: "))
ac= int(input("Area comum: "))
ag= int(input("Area de garagem: "))
pt= (ap+ac+ag)*pa
print(round(pt, 2))