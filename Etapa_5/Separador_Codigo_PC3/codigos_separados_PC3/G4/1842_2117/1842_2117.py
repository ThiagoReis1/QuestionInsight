from math import*

q0=float(input("Qual o valor investido? "))
qf=float(input("Qual o valor pretendido? "))
y=int(input("Anos de duração do investimento: "))

r=(log(qf)-log(q0))/y

print(r)