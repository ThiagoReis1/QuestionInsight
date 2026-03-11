from numpy import*
v = array(eval(input("Alvos:")))
i = 0
total = 0
while i < size(v):
		if v[i] == 1:
			total+=100
		elif v[i] == 2:
			total+=60
		elif v[i] == 3:
			total+=20
		i+=1
print(total)