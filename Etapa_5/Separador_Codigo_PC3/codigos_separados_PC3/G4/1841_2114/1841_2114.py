from math import * 

Qo = float(input("digite o valor do investimento"))
r = float(input("digite a taxa de rendimento de 0.0 e 1.0"))


y = (log(3 * Qo) - log(Qo))/r

print(int(y+1))