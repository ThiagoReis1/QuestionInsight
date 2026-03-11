n = int(input())
cont = 0
acum = 0

while n != 0:
	cont += 1
	if n>0:
		acum +=1
	n = int(input())

print(cont)
print(acum*100/cont)