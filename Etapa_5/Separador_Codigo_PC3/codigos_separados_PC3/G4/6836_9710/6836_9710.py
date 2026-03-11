b = 6.80
c = 11.75
m = 5.90
nome = input().upper()
i=0
t=0
while i < len (nome):
	if nome[i]== "B":
		t=t+b
	if nome[i]== "C":
		t=t+c
	if nome[i]== "M":
		t=t+m
	i=i+1
print(round(t,2))