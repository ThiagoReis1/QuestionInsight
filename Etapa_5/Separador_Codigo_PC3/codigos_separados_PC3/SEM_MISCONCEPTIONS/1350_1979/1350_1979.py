# Universidade Federal do Amazonas
# Curso: Engenharia Elétrica - Eletrônica
# Disciplina: Introdução à Ciência dos Computadores
# Nome: Paulo Victor Nascimento dos Santos
# Data: 09/11/2016

from math import*

# Inserção dos valores de estimativa de árvores, semieixo maior e semieixo menor:
QtdArvores = float(input("Informe a quantidade de arvores por metro quadrado:\n"))
a = float(input("Informe o valor do semieixo maior da elipse:\n"))
b = float(input("Informe o valor do semieixo menor da elipse:\n"))

# Cálculo da área da elipse:
area = pi * a * b

#Quantidade total de árvores na área especificada:
QtdTotal = QtdArvores * area
print(int round((QtdTotal),2))