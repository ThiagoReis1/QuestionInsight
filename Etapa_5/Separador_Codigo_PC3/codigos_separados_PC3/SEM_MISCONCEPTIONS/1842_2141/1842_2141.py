from math import *
valor_investido_por_nausiaca = float(input("Digite o valor investido:"))
valor_pretendido_por_nausiaca = float(input("Digite o valor pretendido:"))
numero_de_anos_do_investimento = int(input("Digite a duração de anos:"))
r = (log(valor_pretendido_por_nausiaca) - log(valor_investido_por_nausiaca)) / numero_de_anos_do_investimento
print(r)