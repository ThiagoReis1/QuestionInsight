from numpy import*
from math import*
n= array(eval(input("digite os valores: ")))

i=0
for t in range(size(n)):
	n[t]= n[t] + 1
	media= log (exp(n[t]+exp(n[n-1]))/exp(n))
	
print(round(media,2))
		  