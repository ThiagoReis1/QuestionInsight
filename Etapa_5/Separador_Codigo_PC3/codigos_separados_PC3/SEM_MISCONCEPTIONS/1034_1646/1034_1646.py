# Carlos Matheus Haddad Braga - matricula 21453480
# Lab de Codificação
# Prova em sala 1
# 16 / 06 / 2016

valor_trocado = float(input("Qual o valor que o cliente entrega em reais"))
taxa_descontada = 12
cotacao_dolar = 3.55
valor_devolvido = (valor_trocado - taxa_descontada) / cotacao_dolar
print(round(valor_devolvido,2))