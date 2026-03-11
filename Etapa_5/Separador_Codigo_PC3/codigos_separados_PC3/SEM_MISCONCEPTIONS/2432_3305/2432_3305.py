#programa que leia
preco_da_area = float(input("entre com o preco da area: "))
#area total do imovel
ap = float(input("entre com o valor da area privativa: "))
ac = float(input("entre com o valor da area comum: "))
ag = float(input("entre com o valor da area da garagem: "))
#valor total do imovel
preco_total = ((ap + ac + ag)*(preco_da_area))
print(round(preco_total, 2))