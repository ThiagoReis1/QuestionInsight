from numpy import*
s = array(eval(input("digite as jogadas:")))
i = 0
x = 0

while i < size(s):
	if s[i]==1:
		x = x + 10
	elif s[i]==2:
		x = x + 5
	elif s[i]==4:
		x = x + 5
	elif s[i]==5:
		x = x + 20
	elif s[i]==6:
		x = x + 10
	i = i + 1
	
print(x)
	

	
