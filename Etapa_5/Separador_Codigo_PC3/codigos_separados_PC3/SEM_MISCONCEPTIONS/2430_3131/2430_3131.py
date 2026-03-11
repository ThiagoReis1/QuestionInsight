capital = float(input("valor total da compra: "))
tempo = int(input("quantidade de parcelas: "))

taxasimples = 3

juros = (capital * taxasimples * tempo) / 100

montante = capital + juros

print (round(montante, 2))