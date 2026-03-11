from numpy import *
#Vetor de entrada:
vetor = input("Digite H (Hortifrut), C (Cereais) ou L (Laticinios): ").upper()
#Varíavel acumuladora e contadora
i = 0
soma = 0
H = 0
C = 0
L = 0
#laço
while i < len(vetor):
   if (vetor[i] == "H"):
      soma += 5.40
      H += 1
   if (vetor[i] == "C"):
      soma += 8.95 
      C += 1
   if (vetor[i] == "L"):
      soma += 4.50
      L += 1
   i += 1
#Resultado
print(round(soma,2), H, C, L)