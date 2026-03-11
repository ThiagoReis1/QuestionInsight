# Monalisa Pereira 21600560
# 16 06 2016
# Avaliacao 01 - Exercicio 01

largura = float(input("Insira a largura da fazenda: "))
comprimento = float(input("Insira o comprimento da fazenda: "))
preco = float(input("Insira o preço por m²: "))

area = largura * comprimento
valor = area * preco

print(round(valor, 2))