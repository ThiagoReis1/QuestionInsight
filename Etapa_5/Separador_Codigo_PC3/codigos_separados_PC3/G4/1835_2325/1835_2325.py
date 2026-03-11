"""
UNIVERSIDADE FEDERAL DO AMAZONAS
DISCENTE: Dave Monteiro Bonates   mat: 21601485
TURMA: Engenharia de Produção
DATA: 04/04/2017 
"""
L = float(input("Comprimento L de um pêndulo: "))
from math import*

#valor da gravvidade
g = 9.8

#fórmula do período de oscilação (T) 
T = 2 * pi* (L/g)**0.5

print(T)
