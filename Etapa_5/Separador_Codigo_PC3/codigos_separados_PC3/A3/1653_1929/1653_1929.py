from numpy import*
vetor=input()


vetor=vetor.split(',')
qtdMC=0
qtdC=0
qtdCM=0
qtdEM=0
qtdE=0


for i in vetor:
   if(i=='AR'):
        qtdMC+=1
   if(i=='BR'):
        qtdC+=1
   if(i=='CL'):
        qtdCM+=1
   if(i=="CO"):
        qtdEM+=1
   if(i=="UY"):
        qtdE+=1


vetorQtd= array([qtdMC,qtdC,qtdCM,qtdEM,qtdE])
maior= maior = vetorQtd[0]
for i in vetorQtd:
    if(i>maior):
      maior =i

print(maior)
print(vetorQtd)