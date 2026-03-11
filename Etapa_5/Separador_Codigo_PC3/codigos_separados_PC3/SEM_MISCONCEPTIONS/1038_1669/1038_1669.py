valor_fixo = 8.50
valor_variavel = 0.03
quantidade_de_ienes = float(input("qual o total de ienes?"))
#valores em moeda devem ser arrendondados em duas casas decimais
ienes_total = (valor_fixo / valor_variavel * quantidade_de_ienes) + valor_fixo
print(round(ienes_total, 2))