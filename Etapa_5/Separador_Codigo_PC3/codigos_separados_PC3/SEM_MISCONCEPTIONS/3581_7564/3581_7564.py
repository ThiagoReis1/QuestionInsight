from numpy import*
itens = array(eval(input("")))
x=0
i=0
while(i<size(itens)):
	if(itens[i]>40.0):
		x=x+itens[i]-2.50
	else:
		x=x+itens[i]
	i=i+1
print(round(x,2))