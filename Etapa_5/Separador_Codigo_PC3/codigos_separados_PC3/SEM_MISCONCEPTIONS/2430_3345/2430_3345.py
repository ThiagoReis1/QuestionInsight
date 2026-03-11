valor = float(input("Valor da compra: "))
tempo = float(input("Quantidade de parcelas: "))

juros = round(float((valor * tempo * 3) / 100), 2)
M = round(float(valor + juros), 2)
print(M)
