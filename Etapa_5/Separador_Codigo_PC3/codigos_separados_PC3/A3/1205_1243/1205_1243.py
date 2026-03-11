from numpy import*

salto = array(eval(input("digite distancia: ")))

recorde = 8.95
i = 0
count = 0
while(i < size(salto)):
	if(salto[i] <= recorde):
		count = salto[i]+ 1
	i = i + 1
else:
	print(recorde)
i = 0
count = 0
while(i < size(salto)):
	if(salto[i] > recorde):
		count = count + 1
	i = i + 1
print(count)