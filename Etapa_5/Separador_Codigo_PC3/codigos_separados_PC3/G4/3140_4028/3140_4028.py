from numpy import *
v = array(eval(input("vetor com n numeros reais positivos:")))
n = 0
m = ((v[n]**5)/(n + 1))**0.2

print(round((sum(m)/size(m)),2))