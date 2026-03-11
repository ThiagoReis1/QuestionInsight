from numpy import*
elev = input()
x = 0
soma = 0
while x < (len(elev)-1):
	soma = abs(elev[x]-elev[x+1])
	x = x+1
print(soma)