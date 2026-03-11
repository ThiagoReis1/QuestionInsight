from numpy import*

a = array(eval(input("vetor de numeros: ")))

c = 0
p = 10000

while(c < size(a)):
	if(a[c] == 1):
		p = p * 2
	elif(a[c] == 2):
		p = p
	elif(a[c] == 3):
		p = p / 2
	elif(a[c] == 4):
		p = p / 4
	c = c + 1
print(round(p, 2))