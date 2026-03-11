from numpy import *
notas=array(eval(input('insira as notas:')))
peso=array([3,4,2,1,4,5])
den=dot(notas,peso)
num=sum(peso)
media=den/num
print(round(media,2))