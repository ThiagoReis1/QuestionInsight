# entradas do peso e quantidade diaria

peso = float(input("peso do saco de racao"))
quantidade = float(input("determine a quantidade diaria de racao em gramas"))
# calculo de quanto gasta em 7 dias
semana = quantidade * 7
# calculo do valor inical menos a semana
resto = peso - semana

print(round(resto, 4))
