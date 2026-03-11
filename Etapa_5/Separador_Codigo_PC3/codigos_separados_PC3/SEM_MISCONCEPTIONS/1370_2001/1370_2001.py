from math import *

qt_req = float(input("Digite a quantidade de poção: "))
snowberry = 8.42 / 100
sais_de_fogo = 19.83 / 100
amanita = 71.75 / 100

qt_snowberry = snowberry * qt_req
print (round(qt_snowberry,2))

qt_sais = sais_de_fogo * qt_req
print (round(qt_sais,2))

qt_amanita = amanita * qt_req
print (round(qt_amanita,2))

