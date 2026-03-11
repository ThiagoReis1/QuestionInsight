x = float(input())
k = int(input())
cont = 1
while (k < cont):
	deno= (x*2+1)
	y = x**deno
	x= x + y/deno
	
	
print(round(x,7))