from numpy import*
custo = array(eval(input("digite custo: ")))

i = 0

while (i < size(custo)):
	if (custo [i] <= 80):
		
		msg = sum(custo)
	else:
		msg = msg - 5
	i = i +1
print (round(msg,2))
	