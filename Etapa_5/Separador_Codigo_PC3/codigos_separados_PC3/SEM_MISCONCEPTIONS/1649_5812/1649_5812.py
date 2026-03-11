from numpy import *

olhos = input().split(',')

cor = zeros(5, dtype=int)

for i in range(0,size(olhos)):
	if olhos[i]== "P":
		cor[0]=cor[0]+1
	elif olhos[i]== "C":
		cor[1]=cor[1]+1
	elif olhos[i]=="M":
		cor[2]=cor[2]+1
	elif olhos[i]== "V":
		cor[3]=cor[3]+1
	else:
		cor[4]=cor[4]+1
		
print(max(cor))
print(cor)
