cliente = float ( input ( "preco: "))
acompanhante = float (input(" preco acompanhente: "))

total = acompanhante - (acompanhante *0.35)
final = cliente + total


print(round(cliente,2))
print(round(total,2))
print(round(final,2))
