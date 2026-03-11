#Dados
pa = int(input("Digite o preco da area:"))
ap = float(input("Digite o valor da area privativa:"))
ac = float(input("Digite o valor da area comum:"))
ag = float(input("Digite o valor da area da garagem:"))

#Calculo
pt = ((ap + ac + ag) * pa)

#Resultado
print(round(pt, 2))