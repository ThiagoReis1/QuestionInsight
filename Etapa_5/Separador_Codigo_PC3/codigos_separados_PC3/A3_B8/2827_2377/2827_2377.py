from numpy import*

notaaluno = array(eval(input("")))
i = 0
notatotal = 0

while i < size (notaaluno):
	if notaaluno[i] > 4 and notaaluno[i] < 5:
		notaaluno[i] = 4
	elif notaaluno[i] > 9 and notaaluno[i] < 10:
		notaaluno[i] = 10

	i = i + 1
	
print(notaaluno)