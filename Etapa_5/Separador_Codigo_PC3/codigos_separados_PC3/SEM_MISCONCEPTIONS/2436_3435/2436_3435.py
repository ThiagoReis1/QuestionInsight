peso = float(input("qual o peso do produto em kg ? : "))
distancia = float(input("qual a distancia em km ? : "))
valor = (peso * 25.00) + (distancia * 0.10)
imposto = valor * (12 / 100)
valor_total = valor + imposto
print(round(valor_total, 2))