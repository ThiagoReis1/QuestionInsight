from numpy import*

notas= array(eval(input("notas : ")))
a=min(notas)
m= (sum(notas)- a) / (size(notas)-1)
print(round(m,2))



