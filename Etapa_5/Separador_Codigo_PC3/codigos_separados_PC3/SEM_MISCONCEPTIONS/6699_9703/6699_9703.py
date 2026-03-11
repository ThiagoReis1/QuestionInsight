taxa_estacionamento = 15.00
tempo = float(input("Digite o tempo de estacionamento: "))
taxa_fixa = 5.00
acrescimo = (taxa_estacionamento * tempo + taxa_fixa) * 20/100
total = taxa_estacionamento * tempo + taxa_fixa + acrescimo
print(round(total, 2))