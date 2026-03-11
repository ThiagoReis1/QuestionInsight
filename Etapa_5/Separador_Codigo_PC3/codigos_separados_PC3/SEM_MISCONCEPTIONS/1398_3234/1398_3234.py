tempo=float(input("qual o tempo de voo "))
if(tempo<=200):
	custo=5000+100*tempo
else:
	custo=8000+100*200+90*(tempo-200)
print(round(custo))