from numpy import*
n = array(eval(input("notas: ")))
pesos=[2,1,5]
v=n*pesos
media=sum(v)/sum(pesos)
print(round(media,2))