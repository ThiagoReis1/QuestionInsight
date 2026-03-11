from numpy import*

f = array(eval(input("Faces: "))
v = zeros(size(f))
while i<size(f):
	if f[i] == 1:
		v[i] = 10
	if f[i] == 2:
		v[i] = 5
	if f[i] == 3:
		v[i] = 0
	if f[i] == 4:
		v[i] = 5
	if f[i] == 5:
		v[i] = 20
	if f[i] == 6:
		v[i] = 10
	i+=1
print(sun(v[i]))