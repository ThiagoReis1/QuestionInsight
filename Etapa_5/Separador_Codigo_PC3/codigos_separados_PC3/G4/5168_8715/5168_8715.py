peso = float(input("peso do saco de racao em gramas: "))
qtde = float(input("quantidade diaria de racao em gramas: "))

semana = 7

r = peso - (qtde*semana)

print(round(r,4))
