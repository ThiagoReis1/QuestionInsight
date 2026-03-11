qtdInicial=int(input())
despesa=int(input())
impostos=int(input())
roubo=int(input())

d=despesa+roubo-impostos
meses=0
while(qtdInicial>0):
    meses=meses+1
    qtdInicial=qtdInicial-d

print(meses)
    
