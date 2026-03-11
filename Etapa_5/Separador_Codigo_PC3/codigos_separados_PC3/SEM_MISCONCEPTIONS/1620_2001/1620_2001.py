from numpy import *
from math import *

tempo = array(eval(input("Digite o tempo gasto: ")))
percentual = array(eval(input("Digite o percentual da torneira: ")))

consumo = ((percentual/100) * 5 * tempo)
	
print (round(consumo,2))

	
										
