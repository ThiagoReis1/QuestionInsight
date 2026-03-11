peso = float(input('Digite o peso do saco:\n'))
qttd = float(input('Digite a quantidade diaria:\n'))

resto = peso - (qttd * 4)

print(round(resto,2))