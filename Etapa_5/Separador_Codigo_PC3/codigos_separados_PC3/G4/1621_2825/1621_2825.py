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
    if(nome[i]=="ARROZ"):
      v0=v0+qnt[i]*1.25
    if(nome[i]=="FEIJAO"):
        v1=v1+qnt[i]*2.60
    if(nome[i]=="BIS"):
        v2=v2+qnt[i]*1.80
    if(nome[i]=="MIOJO"):
        v3=v3+qnt[i]*0.85
    if(nome[i]=="FANTA"):
        v4=v4+qnt[i]*3.20
    v=v0+v1+v2+v3+v4
    i=i+1
print(v)