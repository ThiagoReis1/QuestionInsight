p = float(input('informe o peso da racao em gramas:'))
quant = float(input('informe a quantidade diaria de racao em gramas:'))

resto = p - (quant * 7)
print(round(resto, 3))