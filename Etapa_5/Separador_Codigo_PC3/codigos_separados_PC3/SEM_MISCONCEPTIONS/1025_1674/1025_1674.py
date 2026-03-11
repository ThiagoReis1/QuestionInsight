# Instituto de Computação - UFAM
# Gabriel Rodrigues Afonso Silva - 21551328
# Avaliação 01 - Exercício 01
# 16/06/2016


comprimento = float(input("Qual o comprimento da fazenda?"))
largura = float(input("Qual a largura da fazenda?"))
perimetro = 2 * ( comprimento + largura )
valor_por_metro = float(input("Qual o valor da cerca por metro?"))
valor_total = ( perimetro * valor_por_metro )
print(round(valor_total, 2))