cliente = float(input("passagem do cliente:"))
precoA = float(input("passagem do acompanhante: "))
taxadesconto = (precoA - precoA / 100 * 35 )

desconto = precoA - (precoA * (taxadesconto/100 ))

print(cliente)
print(taxadesconto)
print(cliente + taxadesconto)

