from numpy import*
nome=array(eval(input("")))
qnt=array(eval(input("")))

i=0
v0=0
v1=0
v2=0
v3=0
v4=0
while(i<size(nome)):
    if(nome[i]=="BANANA"):
      v0=v0+qnt[i]*0.97
    if(nome[i]=="BIFE"):
        v1=v1+qnt[i]*2.95
    if(nome[i]=="FEIJOADA"):
        v2=v2+qnt[i]*1.27
    if(nome[i]=="OMELETE"):
        v3=v3+qnt[i]*1.04
    if(nome[i]=="TOMATE"):
        v4=v4+qnt[i]*0.2
    v=v0+v1+v2+v3+v4
    i=i+1
print(v)
