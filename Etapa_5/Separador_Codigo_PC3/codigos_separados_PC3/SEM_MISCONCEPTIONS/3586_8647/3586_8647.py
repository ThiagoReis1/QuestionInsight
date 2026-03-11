from numpy import *

acertos = array(eval(input("Quais foram os aneis acertados?: ")))

i = 0
dados = 0

while i < size(acertos):
	if acertos[i] == 1:
		dados = dados + 100
	if acertos[i] == 2:
		dados = dados + 60
	if acertos[i] == 3:
		dados = dados + 20
	if acertos[i] == 4:
		dados = dados + 0
	
	i += 1
	
	
print(dados)
		