snow = float(input("Digite quantas gramas há de snowberry: "))
sais = float(input("Digite quantas gramas há de sais de fogo: "))
amanita = float(input("Digite quantas gramas há de amanita: "))

potsnow = int(snow/0.31)
potsais = int(sais/0.73)
potamanita = int(amanita/2.64)

quantidades = (potsnow,potsais,potamanita)
pots = min(quantidades)
print("", pots)