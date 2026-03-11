capital = int(input("valor da compra: "))
tempo = int(input("parcelas ao mes: "))

juros = capital * 3 * tempo / 100

montante = capital + juros
print(montante)
