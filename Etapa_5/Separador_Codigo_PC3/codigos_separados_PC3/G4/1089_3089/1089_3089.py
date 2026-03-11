from math import*
v1=float(input("qual o valor da compra1: "))
v2=float(input("qual o valor da compra2: "))
v3=float(input("qual o valor da compra3: "))
l=float(input("qual o limite: "))

vt= v1+v2+v3
if (vt<=l):
   mensagem= "Nao ultrapassou"
else:
   mensagem= "Ultrapassou"
print(round(vt,2))
print(mensagem)