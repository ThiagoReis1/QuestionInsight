preco = float(input("preco ingresso: "))

descontado = preco - (preco*(60/100))

total = preco + descontado

print(round(preco,2))
print(round(descontado,2))
print(round(total,2))