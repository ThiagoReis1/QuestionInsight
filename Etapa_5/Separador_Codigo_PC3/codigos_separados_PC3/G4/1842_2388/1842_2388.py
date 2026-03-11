
from math import*

q0= float(input("valor inicial do investimento : "))
qf= float(input("valor final pretendido :"))
y= int(input("anos de duracao do investimento : "))

r= (log(qf) - log(q0)) / y

print(r)