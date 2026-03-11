peso = float(input("peso"))
quantidade = float(input("quantidade diaria"))

umasemana = float(peso + quantidade) * 7
sobrasemana = float(umasemana * 0.7)
print(round(sobrasemana , 2))

