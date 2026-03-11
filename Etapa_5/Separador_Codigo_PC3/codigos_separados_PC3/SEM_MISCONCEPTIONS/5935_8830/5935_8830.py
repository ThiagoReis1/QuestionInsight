txfixa = 25.00
fretekg = 43.21

peso1 = float(input("peso: " ))
peso2= peso1 * fretekg

icms= (peso2+txfixa) * (62/100)
preco= peso2 + icms + txfixa
print(round(preco,2))