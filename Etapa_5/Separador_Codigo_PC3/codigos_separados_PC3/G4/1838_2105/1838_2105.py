from math import*

R1=int(input("digitar o valor: "))
R2=int(input("digitar o valor: "))
R3=int(input("digitar o valor: "))
Req=(R1 * R2 * R3)/(R1*R2 + R2*R3 + R1*R3)

print(float(Req))