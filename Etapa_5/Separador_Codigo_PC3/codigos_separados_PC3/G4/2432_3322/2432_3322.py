area = float(input("Preco da area: "))
ap = int(input("Area privativa: "))
ac = int(input("Area comum: "))
ag = int(input("Area da garagem: "))

tot = ((ap + ac + ag) * area)

print(float(tot))