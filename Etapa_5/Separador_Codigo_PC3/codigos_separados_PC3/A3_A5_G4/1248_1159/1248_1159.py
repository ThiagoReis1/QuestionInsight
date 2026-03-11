import numpy
n1=float(input("Digite o número:"))
n2=float(input("Digite o número:"))
numeros=[n1,n2]
A=min(n1,n2)
B=max(n1,n2)
v=[A,B]
C = 0.75* A + 0.25* B
C=int(C)
D = 0.25* A + 0.75* B
D=int(D)
v2=[C,D]
print(v2)
print("Eu odeio Python")