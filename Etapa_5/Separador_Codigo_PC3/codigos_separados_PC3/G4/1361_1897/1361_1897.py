#----------------------------------------------
#UNIVERSIDADE FEDERAL DO AMAZONAS
#GIOVANNI VIEIRA PINTO
#----------------------------------------------
#Importar o módulo para trabalhar com as raízes.
from math import*

n = float (input ("Numero de poções: "))
#Calculo das proporções de ingredientes para uma poção:
#Snowberry
s = (5**(1/2)-1)/4
#Sais de Fogo
f = (5 - 2*(5**(1/2)))**(1/2)
#Amanita
a = 5*(5 - 2*(5**(1/2)))
#Determinando a quantidade de cada ingrediente:
qs=(n*s)
qf=(n*f)
qa=(n*a)
#Exibindo o valor na ordem:
print(round(qs,2))
print(round(qf,2))
print(round(qa,2))