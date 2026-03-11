#----------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# VICTOR ALEXANDRE GOMES WEIL - 21603648
# DATA: 27/10/2016
#
#
#----------------------------------
estimativa_de_alunos=float(input("A estimativa de alunos por metro quadrado:"))
comprimento_da_basemaior=float(input("Comprimento da base maior em metros:"))
comprimento_da_basemenor=float(input("Comprimento da base menor em metros:"))
altura_do_trapezio=float(input("Altura do trapezio em metros:"))
x=round(estimativa_de_alunos, 2)
y=round(comprimento_da_basemaior, 2)
z=round(comprimento_da_basemenor, 2)
h=round(altura_do_trapezio, 2)
area_do_trapezio= (h * (y+z)) / 2
total_de_alunos= x * area_do_trapezio

print(int(total_de_alunos))