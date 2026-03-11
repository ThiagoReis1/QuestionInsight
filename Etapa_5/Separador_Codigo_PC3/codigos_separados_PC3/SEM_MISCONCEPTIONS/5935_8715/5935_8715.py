peso = float(input("peso da mercadoria em kg: "))

valor_merc = 43.21
tf = 25

frete = (peso*valor_merc)+tf
total = (frete*62/100)+ frete

print(round(total,2))
