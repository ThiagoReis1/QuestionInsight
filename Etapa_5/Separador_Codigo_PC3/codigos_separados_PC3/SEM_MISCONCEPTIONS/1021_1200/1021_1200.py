#Universidade Federal do Amazonas
#Instituto de Computacao-UFAM
#Departamento:Fisica
#Disciplina:Introducao a Programacao de Computadores(IPC20161)
#Professor:Mario Salvatierra Junior
#Aluno:Frank Lucas Duarte Ozorio
#Numero de matricula:21553797
#Objetivo:Escreever um script em Python na qual dado a medida do lado (a) do hexagono regular,calcular o preco pela metragem quadrada.

#Descricao de variaveis:
#area_hexagono-----------area do hexagono regular
#_a---------------------- medida da aresta do hexagono regular
#custo_fertilizante_por_m2----- custo fertilizante aplicada pela metragem quadrada
#custo_total------ custo da aplicação do fertilizante de acordo com a metragem do hexagono regular

#Plano de calculo:

from math import*

#Medida da aresta do hexagono regular:
_a=float(input("Medida _a do hexagono regular:"))
#Custo fertilizante aplicasda pela metragem quadrada:
custo_fertilizante_por_m2= float(input("Custo do fertilizante:"))

#Area do hexagono regular:
area_hexagono= 3 * sqrt(3) * (_a ** 2)/2

#Custo total:
custo_total= area_hexagono * custo_fertilizante_por_m2

print(round(custo_total,2))


