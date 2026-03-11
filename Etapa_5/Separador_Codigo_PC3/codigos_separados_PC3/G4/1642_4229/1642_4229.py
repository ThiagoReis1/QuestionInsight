from numpy import *
t = array(eval(input("lista de turmas com 5 alunos: ")))
ncinco = 0 # zero contador de cincos
j = 0 #contador para o vetor dfe turmas com cincos
for i in range(size(t)):
   if(t[i]%5==0):
      ncinco = ncinco + 1
p=zeros(ncinco,int)
for i in range(size(t)):
   if(t[i]%5==0):
      p[j] = i
      j= j+1
print(ncinco)
print(p)