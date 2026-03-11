from numpy import*
v = input("Inicial das cores dos olhos: ").upper().split(',')
t = array(zeros(5, dtype=int))
for i in range(size(v)):
	if(v[i] == 'P'):
		t[0] = t[0] + 1
	elif(v[i] == 'C'):
		t[1] = t[1] + 1
	elif(v[i] == 'M'):
		t[2] = t[2] + 1
	elif(v[i] == 'V'):
		t[3]  = t[3] +1
	elif(v[i] == 'A'):
		t[4] = t[4] + 1
print(max(t))
print(t)