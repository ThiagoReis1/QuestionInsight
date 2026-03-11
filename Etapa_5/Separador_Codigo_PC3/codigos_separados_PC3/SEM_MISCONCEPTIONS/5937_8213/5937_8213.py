preco_da_gasolina=2.86
troca_do_oleo=50.00
quantidade_de_litros=float(input("Quantidade de litros abastecidos:"))
antes_do_imposto=(preco_da_gasolina*quantidade_de_litros+troca_do_oleo)
com_o_imposto=(antes_do_imposto+antes_do_imposto*(34/100))
print(round(com_o_imposto,2))