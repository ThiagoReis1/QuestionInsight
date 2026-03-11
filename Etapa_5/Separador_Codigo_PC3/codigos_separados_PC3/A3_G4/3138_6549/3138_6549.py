from numpy import*

v = array(eval(input("")))

cont = 0
soma = 0
media = 0

while(cont < size(v)):
	soma += v[cont]**7
	cont+=1

media = (soma / size(v))**(1/7)

print(round(media, 2))	