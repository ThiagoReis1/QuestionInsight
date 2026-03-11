from math import*

q0 = float(input("investimento do CHICÃO: "))
qf = float(input("lucrão :"))
y = int(input("anos: "))

r = (log(qf) - log(q0))/ y

print(float(r))