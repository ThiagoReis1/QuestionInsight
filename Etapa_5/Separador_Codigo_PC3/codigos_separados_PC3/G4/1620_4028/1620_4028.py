from numpy import *

tb = array(eval(input("vetor com o tempo dos banhos em minutos:")))
pc = array(eval(input("vetor com o percentual de abertura da torneira:")))

v = (5/tb)*pc

print(round(v,2))