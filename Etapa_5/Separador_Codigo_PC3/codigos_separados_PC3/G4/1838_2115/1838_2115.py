from math import*

R1= float(input("Digite o valor:"))
R2= float(input("Digite o valor:"))
R3= float(input("Digite o valor:"))

v1= (R1 * R2 * R3)
v2= (R1 * R2)+(R2 * R3)+(R1 *R3)

Req= (v1 / v2)

print(Req)