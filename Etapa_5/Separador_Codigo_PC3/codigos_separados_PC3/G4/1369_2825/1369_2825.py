#ingredientes
D1 = float(input("Quantas gramas de chifre de touro:"))
D2 = float(input("quantas gramas de ouro em pó:"))
D3 = float(input("quantas gramas de oleo de dwarven:"))
# ingredientes necesssarios
A= D1/4
B = D2/3.14
C = D3/10

#preparo da porção

porcao = min(A,B,C)
print (int(porcao))
