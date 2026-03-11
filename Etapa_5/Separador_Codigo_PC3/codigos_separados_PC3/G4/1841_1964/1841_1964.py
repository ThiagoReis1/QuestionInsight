from math import*
Q0 = float(input("Digite o valor investido em reais: "))
r = float(input("Taxa anual de rendimento: "))
Qf = 3*Q0
y=int((log(Qf)-log(Q0))/r)
print(y+1)