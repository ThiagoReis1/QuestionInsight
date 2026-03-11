#Elysmara Coutinho de oliveia
#data:16/06/2016
#avaliação

quilo=float(input("Digite aqui quantos quilos voce quer levar:"))

taxa_fixa=25
cada_quilo=43.21

custo_frete=quilo*cada_quilo+taxa_fixa

icms=62/100
total= custo_frete*icms + custo_frete

print(round(total,2))

