#entrada
x = float(input())

#saida
if((x <= -1) or (x >= 1)):
	fx = x * x
if(((-1 < x) and (x < 0)) or ((0 < x) and (x < 1))):
	fx = x
if(x == 0):
	fx = 1
	
print(round(fx, 4))