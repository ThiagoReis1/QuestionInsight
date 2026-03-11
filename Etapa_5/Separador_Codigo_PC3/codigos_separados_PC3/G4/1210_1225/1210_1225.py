from numpy import *

vetor =(eval(input("Informe o primeiro vetor: ")))
i=0
cont=0
r=74.08
while(i<len(vetor)):
   if(vetor[i]<r):
       cont=cont+1
   i=i+1
print(r,cont)