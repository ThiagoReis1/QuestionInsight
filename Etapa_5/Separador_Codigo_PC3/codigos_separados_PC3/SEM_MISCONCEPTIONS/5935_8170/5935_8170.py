peso = float(input("Digite o peso da mercadoria: "))

frete = (peso * 43.21) + 25.00
t = frete * 0.62
total = frete + t

print(round( total, 2))