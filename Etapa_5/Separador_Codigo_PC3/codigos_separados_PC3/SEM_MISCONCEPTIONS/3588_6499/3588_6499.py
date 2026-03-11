total = 10000
acertos = eval(input())
for i in acertos:
	if i == 1:
		total*=2
	elif i == 2:
		total+=0
	elif i == 3:
		total/=2
	else:
		total/=4
print(round(total,2))	