peso = float(input('Digite o peso da mercadoria:'))

frete = (peso * 43.21) + 25.00
icms = frete * 0.62

total = frete + icms


 



print(round(total, 2))