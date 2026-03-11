from math import *
q0 = float(input("Qual o Valor Inicial de investimento? "))
qf = float(input("qual o Valor Final pretendido? "))
y = float(input("Quantos Anos deseja investir? "))
r = (log(qf) - log(q0)) / y
print(r)