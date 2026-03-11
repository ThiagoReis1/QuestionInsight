#Julia Pacheco
#Av 01 - Ex02

#peso da mercadoria
peso = float(input("Digite o peso da mercadoria: "))
#preco por quilo
precoKg = 43.21
#taxa fixa
taxa = 25
#valor frete
frete = (peso * precoKg) + taxa
#valor do ICMS
icms = frete * 0.62 
#valor a ser pago
valorApagar = frete + icms
print(round(valorApagar,2))