from numpy import *
from numpy.linalg import *
tempos = array(eval(input("Tempos de banho:")))
percent = array(eval(input("Percentual:")))
conta= (tempos*percent)
contaJ = (conta/100)
contaF= (contaJ*5)
resposta = sum(contaF)
print(round(resposta, 2))