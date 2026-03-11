from numpy import*
vetor=input()


vetor=vetor.split(',')
qtdMC=0
qtdC=0
qtdCM=0
qtdEM=0
qtdE=0
qtdME=0

for i in vetor:
   if(i=='MC'):
        qtdMC+=1
   if(i=='C'):
        qtdC+=1
   if(i=='CM'):
        qtdCM+=1
   if(i=="EM"):
        qtdEM+=1
   if(i=="E"):
        qtdE+=1
   if(i=="ME"):
        qtdME+=1

vetorQtd= array([qtdMC,qtdC,qtdCM,qtdEM,qtdE,qtdME])
maior= maior = vetorQtd[0]
for i in vetorQtd:
    if(i>maior):
      maior =i

print(maior)
print(vetorQtd)