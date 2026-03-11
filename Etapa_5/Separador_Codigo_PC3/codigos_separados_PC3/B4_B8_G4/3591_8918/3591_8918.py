from numpy import*
face = array(eval(input("face tirada: ")))

s = 0

for i in face:
	if i == 1:
		s = s + 10
	elif i == 2:
		s = s + 5
	elif i == 3:
		s = s + 10
	elif i == 4:
		s = s + 5
	elif i == 5:
		s = s + 10
	elif i == 6:
		s = s + 5
print(s)