from numpy import*
nota = array(eval(input("digite: ")))
media = nota[0]*3 + nota[1]*5 + nota[2]*1
peso = 3,5,1
resul = sum(media)/sum(peso)
print(round(resul, 2))
