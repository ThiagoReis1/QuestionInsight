litro = float(input())
preco_litro = 2.86
oleo = 50.00
taxa = 0.34

total = litro * preco_litro + oleo 
icms = total * taxa
soma = total + icms

print(round(soma, 2))