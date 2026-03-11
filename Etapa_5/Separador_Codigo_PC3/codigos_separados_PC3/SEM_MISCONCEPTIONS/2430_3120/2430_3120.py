
capital = float(input("Capital"))
tempo = float(input("tempo"))

taxa_de_juros = 300 / 100

juros = capital * taxa_de_juros * tempo / 100

m = capital + juros 

print(round(m, 2))