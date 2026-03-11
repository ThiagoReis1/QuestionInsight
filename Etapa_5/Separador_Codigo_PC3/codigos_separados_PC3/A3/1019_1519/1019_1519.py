# Avaliação Parcial 1

area_fazenda = float(input("Qual a area da fazenda?"))
custo_aplicacao = float(input("Custo total do servico?"))
custo_por_m2 = float(input("Qual o valor por m2?"))
area_fazenda = comprimento_fazenda * largura_fazenda
custo_total = custo_material * area_fazenda
custo_total = round((area_fazenda*custo_por_m2),2)
print (custo_total)