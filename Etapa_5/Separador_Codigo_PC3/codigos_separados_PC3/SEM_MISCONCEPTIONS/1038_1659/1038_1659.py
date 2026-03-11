# Leandra de Souza Mendes - Matricula 21554018
# Data 16 / 06 / 2016

quantia_reais = float(input("Digite a quantia em reais: "))
taxa_fixa = 8.50
cotacao_ienes = 0.03

restante = quantia_reais - taxa_fixa

total_ienes = restante / cotacao_ienes

#Arredondar o valor em duas casas decimais
#para representar os centavos

print(round(total_ienes, 2))

