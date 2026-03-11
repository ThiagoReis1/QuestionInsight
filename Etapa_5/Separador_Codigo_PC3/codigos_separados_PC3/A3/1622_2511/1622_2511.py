#Lotação
from numpy import*

entram_onibus = array(eval(input("Quais pessoas: ")))
sairam_onibus = array(eval(input("Quais pessoas: ")))
maximo = 75
total = sum(entram_onibus) - sum(sairam_onibus)
print(total)