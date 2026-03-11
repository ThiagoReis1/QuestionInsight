#valor do pedagio: 9.80
#taxa fixa: 20
#aumeto: 15%
praca = float(input())
valor = (praca * 9.80 + 20)

total = valor + valor *(15/100)

print(round(total,2))
