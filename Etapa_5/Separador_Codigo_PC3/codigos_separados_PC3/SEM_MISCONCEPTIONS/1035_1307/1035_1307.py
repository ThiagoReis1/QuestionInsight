# Problema: converter reais para euro

# Variaveis

servico = 15.0
euro = 3.96

valor = float(input("Digite o valor a ser convertido: "))

x = valor - servico
y = x / euro

print(round(y,2))