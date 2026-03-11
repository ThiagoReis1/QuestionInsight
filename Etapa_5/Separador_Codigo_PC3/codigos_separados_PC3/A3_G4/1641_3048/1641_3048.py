from numpy import*
t = array(eval(input("quantas turmas: ")))
z = zeros(3, dtype=int)

ap = 0

for i in range(size(t)):
	if(t[i] % 3 == 0):
		v = ap + 1
print(v)
	
	