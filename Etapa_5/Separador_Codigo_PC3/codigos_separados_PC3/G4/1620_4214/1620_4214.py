from numpy import *

a= array(eval(input("Tempo:")))
b= array(eval(input("Porcentagem:")))

c1= a*b
c2= c1/100
c3= c2*5

a=sum(c3)
print(round(a,2))