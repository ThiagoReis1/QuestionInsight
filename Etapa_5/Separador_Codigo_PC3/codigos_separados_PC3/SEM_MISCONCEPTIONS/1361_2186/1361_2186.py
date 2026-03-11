from math import *
porcao=float(input("digite quantidade de porçoes "))


#quantidade de cada porção
q_snowberry= porcao*(sqrt(5)-1)/4
q_sais= porcao*sqrt(5-2*sqrt(5))
q_amanita=porcao*5*(5-2*sqrt(5))

print(round(q_snowberry,2))
print(round(q_sais,2))
print(round(q_amanita,2))