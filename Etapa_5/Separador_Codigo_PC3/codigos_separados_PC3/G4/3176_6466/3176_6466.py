from numpy import*
a= input('Qual a palavra?: ')

v = 'aeiou'
qv = 0 #vogal

for i in range(len(a)) :
	for j in range(len(v)):
		if a[i] == v[j]:
			qv = qv + 1

qc = abs(len(a) - qv) #consoante
	
print(qv)
print(qc)