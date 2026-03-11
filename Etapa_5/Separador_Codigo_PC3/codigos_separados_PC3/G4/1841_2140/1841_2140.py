from math import*
Qo = float(input("Valor inicial investido"))
r = float(input("Taxa de Rendimento :"))
Qf = Qo * 3
Y= ((log(Qf) -log(Qo) )/r) + 1
print (int(Y))