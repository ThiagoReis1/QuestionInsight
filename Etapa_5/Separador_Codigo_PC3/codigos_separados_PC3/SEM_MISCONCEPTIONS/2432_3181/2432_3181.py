p_area = float(input("Preco da area por m2: "))
ap= float(input("area privativa por m2: "))
ac= float(input("Area comum: "))
ag = float(input("Area de garagem: "))


p_total = ((ap + ac + ag) * p_area)
print(float(round(p_total, 2)))