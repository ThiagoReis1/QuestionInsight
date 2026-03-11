from numpy import*
tempo = array(eval(input('tempo de chegada do corredor  ')))
x=size(tempo)

v=0
while(v<x):
	if(tempo[v]==max(tempo)):
		t=tempo[v]
		print(v)
	v=v+1