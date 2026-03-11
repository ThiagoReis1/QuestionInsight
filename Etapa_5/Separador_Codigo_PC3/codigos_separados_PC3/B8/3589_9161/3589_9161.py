from numpy import *

acertos = array(eval(input(" : ")))
total = 0
i = 0
while i < size(acertos) :
	if acertos[i] == 1 :
		total += 80
	elif acertos[i] == 2 :
		total += 40
	elif acertos[i] == 3 :
		total += 20
	elif acertos[i] == 4 :
		total += 10
	i += 1
print(total)