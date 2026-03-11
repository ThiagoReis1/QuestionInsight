
pcliente = float(input())
pacom = float(input())

taxades = 35
desconto = pacom - (pacom * (taxades / 100))       #preco acompanhate (desconto)
total = pcliente + desconto

print(round(pcliente, 2))
print(round(desconto, 2))
print(round(total, 2))

