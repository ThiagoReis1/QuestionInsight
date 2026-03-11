peso = float(input("Peso da mercadoria: "))

quilo = 43.21
taxa = 25

custo = ( peso * quilo ) + taxa

#icms = 62%
icms = custo/100 * 62

total = custo + icms

print(round( total ,2))