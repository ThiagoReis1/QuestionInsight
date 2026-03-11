R1=float(input("valor da resistencia R1:"))
R2=float(input("valor da resistencia R2:"))
R3=float(input("valor da resistencia R3:"))

numerador = R1*R2*R3
denominador=(R1*R2)+(R2*R3)+(R1*R3)
req = numerador/denominador
print(req)