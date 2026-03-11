from math import *
ang = eval(input(" "))
k = int(input(" "))
cont = 0
res = 0
expo = 1
x = 0
deno = 1
while(cont< k):
	x = (ang**expo)/(factorial(deno))
	if(cont%2!=0):
		x = x *(-1)
	res = res +x
	cont+=1
	expo+=2
	deno+=2
print(round(res,10))