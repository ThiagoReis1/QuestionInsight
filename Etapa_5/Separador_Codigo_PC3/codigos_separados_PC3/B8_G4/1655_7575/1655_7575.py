from numpy import*

v=input("sigla dos estados: ").upper().split(',')

e=zeros(5, dtype=int)
for x in v:
	if x=="AC":
		e[0]=e[0]+1
	elif x=="AM":
		e[1]=e[1]+1
	elif x== "PA":
		e[2]=e[2]+1
	elif x== "RO":
		e[3]=e[3]+1
	elif x== "RR":
		e[4]=e[4]+1
print(max(e))
print(e)
