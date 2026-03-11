cliente = float(input("valor cliente"))

acompanhante = float(input("valor acompanhante"))

desconto = acompanhante - (acompanhante * 0.35)

total = desconto + cliente

print (round(cliente,2))
print (round(desconto,2))
print (round(total,2))
