#################################################################
# Paulo Sergio da Silva Freitas
# Avaliação Parcial 02
# Programa: Verifica se um numero atende determinada propriedade
#################################################################
import math
numero = int(input("leia o numero : "))
parte1=(numero//10000)
parte2=((numero%10000)//100)
parte3=((numero%100))
cubo1 = parte1**3
cubo2 = parte2**3
cubo3 = parte3**3
soma=(cubo1+cubo2+cubo3)
if (numero == soma):
  print("X atende a propriedade")
else:
  print(soma)	
  
