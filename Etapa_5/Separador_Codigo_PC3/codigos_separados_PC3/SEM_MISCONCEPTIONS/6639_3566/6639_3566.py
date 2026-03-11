from numpy import *

string = input().upper()

cont = 0

if 'M' not in string:
	print('nao achei')
else:
	while(cont < len(string)):
		if(string[cont] == 'M'):
			print(cont)

		cont+=1



