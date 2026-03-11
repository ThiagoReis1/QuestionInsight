preco1 = float(input("preco da area em m quadrados: "))
valorap= int(input("area privaticva em m quadrados: "))
valorac= int(input("area comum em m quadrados: "))
valorag= int(input("area da garagem em m quadraos: "))

precototal= ((valorap + valorac + valorag) * preco1)
print(round(precototal, 2))