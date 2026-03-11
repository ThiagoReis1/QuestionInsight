from math import * 
p= float(input("digite o peso da espada:"))
qf= 2**(1+p/1000)
qs= p*(pi**2)/3141
qd= 2*sqrt(p/40)
print (round(qf,2))
print (round(qs,2))
print (round(qd,2))