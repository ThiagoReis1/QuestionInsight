f = int(input('Face? '))
f6 = 0
while f != -1:
	if f == 6:
		f6 = f6 + 1
		f = int(input('Outra face: '))
	elif f == 1 or f == 2 or f == 3 or f == 4 or f == 5: 
		f = int(input('Outra face: '))
print(f6)