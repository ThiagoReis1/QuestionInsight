from numpy import *

cod = array(eval(input("codigo")))
x = size(cod)
s = zeros(x,dtype=int)

for i in range(size(cod)):
	if cod[i] == 9:
		s[i] = 0
	if cod[i] == 1:
		s[i] = 2
	if cod[i] == 2:
		s[i] = 3
	if cod[i] == 3:
		s[i] = 4
	if cod[i] == 4:
		s[i] = 5
	if cod[i] == 5:
		s[i] = 6
	if cod[i] == 6:
		s[i] = 7
	if cod[i] == 7:
		s[i] = 8
	if cod[i] == 8:
		s[i] = 9
	if cod[i] == 0:
		s[i] = 1
print(s)


# while cod[i] <= 9:
