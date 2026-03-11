# Nome: Eduardo Marques da Costa - Matricula:21553777
# Lab de Codificacao 1
# Exercicio 1
# 16 / 06 / 2016

largura_do_terreno = float(input(" Qual a largura do terreno em metros? "))

comprimento_do_terreno = float(input(" Qual o comprimento do terreno em metros? "))

custo_de_construcao = float(input(" Qual o custo do material por metro? "))

#cálculo do perímetro do terreno
perimetro_do_terreno = 2 * (largura_do_terreno + comprimento_do_terreno)

custo_total = perimetro_do_terreno * custo_de_construcao

#arredonda duas casas décimais para representar os centavos
print(round(custo_total,2))