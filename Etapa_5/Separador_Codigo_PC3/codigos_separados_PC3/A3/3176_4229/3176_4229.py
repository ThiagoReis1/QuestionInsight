from numpy import *
vetor=str(input())
vogal = 0
cons = 0
print(vetor)
for i in range(size(vetor)):
   if (vetor[i]=='a'):
      vogal = vogal + 1
print(vogal)