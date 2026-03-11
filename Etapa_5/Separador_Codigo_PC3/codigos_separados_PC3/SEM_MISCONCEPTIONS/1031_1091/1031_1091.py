#Litro gasolina = 2,86 reais 
#Serviço de troca de oleo = 50,00
#Imposto = 34% 
from math import*
litros = float(input("Quantos litros de gasolina? "))
oleo = 50.00
preco_litro = 2.86
total = (oleo+litros*preco_litro)
total2 = total+total*0.34
print(round(total2,2))