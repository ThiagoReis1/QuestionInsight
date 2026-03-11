from numpy import*
m=floa(input("Ler n:"))
tot=0
for i in range (size(m)):
	tot=tot+(i+1)*m[i]
for i in range(notas):
	tot=tot/size(m)
print(round(m,2))
	