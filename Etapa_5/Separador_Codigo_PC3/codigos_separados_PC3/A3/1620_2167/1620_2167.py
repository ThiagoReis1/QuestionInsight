from numpy import *
tempo = array(eval(input("Digite o tempo de banho: ")))
percentual = array(eval(input("Digite o percentual: ")))
Semana1 = tempo[0]
Semana2 = tempo[1]
Semana3 = tempo[2]
Semana4 = tempo[3]
SemanaA = percentual[0]
SemanaB = percentual[1]
SemanaC = percentual[2]
SemanaD = percentual[3]
total = (5 * Semana1 + 2.5 * SemanaA) + 12
print(total)