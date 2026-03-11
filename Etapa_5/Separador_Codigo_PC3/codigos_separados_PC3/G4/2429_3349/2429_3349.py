# Cardapio:
op = 6.90
g = 2.50
b = 3.00

# Guarnições incluidas pelo cliente:
g0 = int(input("Insira a quantidade de guarnicoes: ") )
b0 = int(input("Insira a quantidade de bebidas: ") )

# Calculo
ValorTotal = op + g * g0 + b * b0

print(round(ValorTotal , 2))