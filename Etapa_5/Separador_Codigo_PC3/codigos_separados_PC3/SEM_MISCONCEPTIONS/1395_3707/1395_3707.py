a = float(input())
if(a<=1000):
	valor = (a*0.05)
else:
	valor = 50 + (a-1000)*0.1
print(round(valor,2))
