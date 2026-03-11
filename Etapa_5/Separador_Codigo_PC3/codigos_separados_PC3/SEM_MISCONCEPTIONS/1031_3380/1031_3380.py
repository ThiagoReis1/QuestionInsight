gasolina = 2.86
troca_de_oleo = 50.00
valor = float(input())
icms = 34/100

quantidade = (troca_de_oleo + gasolina * valor )*icms + troca_de_oleo + gasolina * valor 
print(round(quantidade,2))