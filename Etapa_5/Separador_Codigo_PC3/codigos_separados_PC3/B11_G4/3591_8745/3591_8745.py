from numpy import*
d = array(eval(input("Digite as faces: ")))
s = 0
i = 0
while i < size(d):
	if d[i] == 1:
		s = s + 10
	if d[i] == 2:
		s = s + 5
	if d[i] == 3:
		s = s + 10
	if d[i] == 4:
		s = s + 5
	if d[i] == 5:
		s = s + 10
	if d[i] == 6:
		s = s + 5
	i = i + 1
print(s)