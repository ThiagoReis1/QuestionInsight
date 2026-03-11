from numpy import *

v = array(eval(input("andares onde parou: ")))

c = 0
caminho = 0

while c < size(v)-1:
	
	caminho =caminho +  abs(v[c]-v[c+1])
	
	c = c + 1
	
print(caminho)