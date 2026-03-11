tempo = float(input("Diga o tempo :"))
if(tempo<=200):
	custo=5000+(tempo*100)
else:
	custo=8000+(200*100)+((tempo-200)*90)
	
print(round(custo,2))