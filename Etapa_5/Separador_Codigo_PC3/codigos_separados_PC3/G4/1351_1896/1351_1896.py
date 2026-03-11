import math
M=float(input("Quantidade de maçãs por metro quadrado: "))
A=float(input("informe o comprimento da aresta: "))
AH=(((3*math.sqrt(3))*math.pow(A,2))/2)*M
print(int(AH))