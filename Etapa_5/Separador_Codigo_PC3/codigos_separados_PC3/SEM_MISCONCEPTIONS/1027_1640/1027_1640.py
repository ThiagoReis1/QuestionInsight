# Nome: Eduardo Marques da Costa - Matricula:21553777
# Lab de Codificacao 1
# Exercicio 2
# 16 / 06 / 2016

kwh_gastos = float(input(" Quantos kWh foram gastos? "))

preco_do_kwh = 0.43

taxa_de_iluminacao_publica = 10

icms = (((kwh_gastos * preco_do_kwh) + taxa_de_iluminacao_publica) / 100) * 25

valor_da_conta = kwh_gastos * preco_do_kwh + taxa_de_iluminacao_publica + icms

print(round(valor_da_conta,2))