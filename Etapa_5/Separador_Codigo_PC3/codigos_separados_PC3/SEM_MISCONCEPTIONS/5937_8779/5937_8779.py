qtde = float(input("didite um numero: "))
preco_g = 2.86 * qtde
preco_o = 50.
soma = preco_g + preco_o
ICMS = soma * 34/100
total = soma + ICMS
print(round(total, 2))