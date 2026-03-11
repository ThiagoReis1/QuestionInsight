from numpy import*

acertos = array(eval(input('digite os acertos:')))
pts= 0
i=0

while i < size(acertos):
	if acertos[i] == 1:
		pts += 100
	elif acertos[i]== 2:
		pts += 60
	elif acertos[i] == 3:
		pts += 20
	i=i+1
print(pts)
	
	