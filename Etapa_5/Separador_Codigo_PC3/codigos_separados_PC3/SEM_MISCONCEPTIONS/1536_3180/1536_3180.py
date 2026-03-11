k = int(input(""))
from math import *

contadora = 1
neperiano = 1

while ( contadora != k):
	aproximacao = 1 / factorial(contadora)
	neperiano = aproximacao +  neperiano 
	contadora = contadora + 1
	
neperiano2 = neperiano

print(round(neperiano2,8))