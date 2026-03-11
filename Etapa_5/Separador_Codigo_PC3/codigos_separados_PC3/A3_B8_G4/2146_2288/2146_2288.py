s = input()
w = ""
a = 0
b = 0
for i in s:
	if i.islower() == True:
		w = w + i.upper()
	elif i.isupper() == True:
		w = w + i.lower()
print(w)
	
	
	