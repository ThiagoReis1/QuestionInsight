#Ellen Barros de Almeida

from math import*

consumo = float(input("Digite o consumo em KWh: "))

valor_conta = (0.43 * consumo + 10.0)

valor_total = (valor_conta * 0.25 + valor_conta)

print(round(valor_total, 2))