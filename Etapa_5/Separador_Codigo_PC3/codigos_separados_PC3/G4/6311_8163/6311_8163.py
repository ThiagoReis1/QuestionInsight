from numpy import*

p= input("digite os produtos: ").upper()
i=0
pc=0
pe=0
pp=0
t=0
while(i<len(p)):
	if p[i]=="C":
		t = t + 10.50
		pc=pc+1
	if p[i]=="E":
		t = t + 8.75
		pe=pe+1
	if p[i]=="P":
		t = t + 17.90
		pp=pp+1	
	i=i+1
print(round(t,2), pc, pe, pp)