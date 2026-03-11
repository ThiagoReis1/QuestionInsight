preco_m2 = float(input('preço do m2: '))
ap = float(input('area privativa: '))
ac = float(input('area comum: '))
ag = float(input('area da garagem: '))
valor_total = ((ap +ac + ag))*preco_m2
print(round(valor_total, 2))