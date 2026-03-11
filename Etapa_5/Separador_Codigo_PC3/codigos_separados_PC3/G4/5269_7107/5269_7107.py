n = int(input())
qn = 0
mt = 0

while(n != 0):
	
	if(n % 3 == 0):
		
		mt = mt + 1
		
	qn = qn + 1
	n = int(input())
p = (mt * 100) / qn

print(qn)
print(round(p, 2))