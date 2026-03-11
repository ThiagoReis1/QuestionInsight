n = float(input())
if n>=-100 and n<0:
	print(round(-1/n,4))
elif n>0 and n<=100:
	print(round(1/n,4))
else:
	print("entrada invalida")
