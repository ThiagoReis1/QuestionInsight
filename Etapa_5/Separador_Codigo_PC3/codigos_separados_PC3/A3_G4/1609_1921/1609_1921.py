from numpy import*
pd = array(eval(input()))
pn = input("quantidade de cada produto: ").upper()
i = 0
a = 0
novon = ''
while(i < size(pn)):
	if(pd[i].upper() == PLEGUICA):
		a = i
	i = i + 1
print(a)
