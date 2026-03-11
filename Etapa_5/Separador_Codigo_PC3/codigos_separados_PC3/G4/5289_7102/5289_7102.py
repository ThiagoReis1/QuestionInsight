n = int(input())

cont = 0
qnt = 0

while(n != -1):
	
	if(n == 6):
		cont = cont + 1
	
	n = int(input())
	qnt = qnt + 1
	s = (cont / qnt) * 100
	
print(qnt)
print(round(s,2))