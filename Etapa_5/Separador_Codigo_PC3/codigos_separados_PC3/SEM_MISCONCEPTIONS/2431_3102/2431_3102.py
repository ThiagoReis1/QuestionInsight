cliente = float(input("preco cliente:"))
acompanhante = float(input("preco acompanhante:"))

desconto= acompanhante - (acompanhante * (35/100))
total= desconto + cliente

print(cliente)
print(desconto)
print(total)

