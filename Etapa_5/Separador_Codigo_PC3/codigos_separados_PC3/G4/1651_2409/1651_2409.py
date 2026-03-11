from numpy import *
s = input("tom de pele: ").upper().split(',')
i = 0
mc = 0
c = 0
cm = 0
em = 0
e = 0
me = 0
vet = zeros(6, dtype=int)
while(i < len(s)):
	if(s[i] == "MC"):
		mc = mc + 1
	elif(s[i] == "C"):
		c = c + 1
	elif(s[i] == "CM"):
		cm = cm + 1
	elif(s[i] == "EM"):
		em = em + 1
	elif(s[i] == "E"):
		e = e + 1
	else:
		me = me + 1
	i = i + 1
vet[0] = mc
vet[1] = c
vet[2] = cm
vet[3] = em
vet[4] = e
vet[5] = me
print(max(vet))
print(vet)
