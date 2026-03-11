from numpy import*
pontos = array(eval(input('diga quais aneis foram acertados:')))
x=size(pontos)
y=0
z=0
while(y<x):
	if(pontos[y]==1):
		z=z+80
	if(pontos[y]==2):
		z=z+40
	if(pontos[y]==3):
		z=z+20
	if(pontos[y]==4):
		z=z+10
	y=y+1
print(z)
		
		