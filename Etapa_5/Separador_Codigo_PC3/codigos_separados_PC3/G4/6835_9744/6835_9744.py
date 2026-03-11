tig1 = input()
tig = tig1.upper()
a = 0
b = 0
while(a<len(tig)):
	if(tig[a]=="B"):
		b += 3.75
	if(tig[a]=="C"):
		b+= 7.90
	if(tig[a]=="E"):
		b+= 9.85
	a+=1
print(round(b, 2))