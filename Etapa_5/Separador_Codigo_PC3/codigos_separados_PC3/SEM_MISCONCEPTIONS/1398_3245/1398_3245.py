t = float(input())

if (t<=200):
	custo = 5000 + 100*t
else:
	custo = 8000 + 100*200 + 90*(t-200)
	
print(round(custo,2))