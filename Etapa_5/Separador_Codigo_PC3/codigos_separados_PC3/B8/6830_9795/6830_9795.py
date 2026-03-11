from numpy import*

produto = input("produto: ")
total = 0
i = 0
while i < len(produto):
	if produto[i] =='H':
		total = total + 3.85 
	if produto[i] =='L':
		total = total + 2.95  
	elif produto[i] =='E':
		total = total + 7.90 
	i = i + 1
print(round(total, 2))