from numpy import*

tempos=array(eval(input("Tempos: ")))
abertura=array(eval(input("Abertura: ")))

i=0
soma=0

while i < size (tempos):
	soma=soma+tempos[i] * (abertura[i]/100)*5
	i=i+1
	
print(round(soma,2))

