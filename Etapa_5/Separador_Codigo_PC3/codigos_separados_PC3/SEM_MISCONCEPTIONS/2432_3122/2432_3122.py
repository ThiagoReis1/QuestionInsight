preco = float(input("Insira o preco da area: "))
ap = float(input("Insira a area privativa: "))
ac = float(input("Insira a area comum: "))
ag = float(input("Insira a area de garagem: "))

total = ((ap + ac + ag)) * preco

print(round(total, 2))