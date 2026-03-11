# faça seu código aqui!
tempo = float(input())
if(tempo<2):
	total = 5+1.25
elif(tempo == 2):
	total = 5+2.25
elif(tempo>2):
	total = 5+3.25
print(round(total, 2))