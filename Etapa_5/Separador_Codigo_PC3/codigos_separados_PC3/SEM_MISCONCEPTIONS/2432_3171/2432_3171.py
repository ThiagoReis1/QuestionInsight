preco = float(input("Informe o preco da area: "))
ap = float(input("Informe a area privativa: "))
ac = float(input("Informe a area comum: "))
ag = float(input("Informe a area da garagem: "))

p_total = ((ap + ac + ag)*preco)

print(round(p_total, 2))
