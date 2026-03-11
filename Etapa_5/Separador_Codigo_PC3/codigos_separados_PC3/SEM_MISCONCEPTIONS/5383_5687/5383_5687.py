from numpy import *

palavra = input("")
total = 0 
i = 0 

while(i< len(palavra)):
	if palavra[i] == "A" or palavra[i] == "E" or palavra[i] == "I" or palavra[i] == "O" or palavra[i] == "U":
		total = total + 0.12
	else:
		total = total + 0.18
	i = i + 1
print(round(total, 2))