from numpy import*
produtos = input("digite os produtos:")
i = 0 
qa = 0
ql = 0
qp = 0
for produtos in produtos:
	if produtos == 'A':
		i+= 16.75
		qa += 1
	elif produtos == 'L':
		i+= 4.60
		ql+=1
	elif produtos == 'P':
		i+=2.85
		qp+=1
print(round(i,2))
print(qa, ql, qp)

		
		
		