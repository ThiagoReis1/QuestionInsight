from math import*

q0 = float(input("valor inicial: "))
qf = float(input("valor final: "))
y = int(input("anos de investimento: "))

a = log(qf) - log(q0)

r = a/y

print(r)