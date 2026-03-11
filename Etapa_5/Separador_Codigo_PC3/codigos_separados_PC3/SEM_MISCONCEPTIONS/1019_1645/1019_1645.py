# Bruno Lopes de Lima
# 21457257
# Avaliação 01 - Variaveis e Estrutura Sequencial de Programacao
# 16 / 06 / 2016

largura_fazenda = float(input("Qual a largura da fazenda?"))
comprimento_fazenda = float(input("Qual o comprimento da fazenda?")) 
area_fazenda = ( largura_fazenda * comprimento_fazenda)
custo_fazenda_por_m2 = float(input("Qual o valor cobrado por m2?"))
valor_total = round((area_fazenda * custo_fazenda_por_m2),2)
print(valor_total)