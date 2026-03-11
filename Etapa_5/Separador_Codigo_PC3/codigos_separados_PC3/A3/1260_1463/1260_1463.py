from numpy import *

p = float(input())
x = array(eval(input()))
y = array(eval(input()))

t = p/(p+1)
norma1 = 0
norma2 = 0

for i in range(0,size(x)):
	x[i] = x[i] - y[i]
	
for i in range(0,size(x)):
	norma1 = norma1 + abs(x[i])**t 
	#norma2 = norma2 + abs(y[i])**t

norma1 = pow(norma1,1/t)
#norma2 = pow(norma2,1/t)
#print ("t:",t)
#print("norma1:",norma1)
#print("norma2:",norma2)
#print ("soma:", norma1 + norma2)
print (round(norma1,4))