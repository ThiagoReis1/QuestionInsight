peso = float(input("digite o peso em gramas:"))
quantidade = float(input("digite a quantidade diaria em gramas:"))
consumo = quantidade * 4
total = peso - consumo

print(round(total, 2))