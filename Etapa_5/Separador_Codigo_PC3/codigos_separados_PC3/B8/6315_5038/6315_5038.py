produto = input("produto: ").upper()
p = 0
total = 0
i = 0
m = 0 
s = 0
while(p<len(produto)):
	if(produto[p]=="I"):
		total = total+3.75
		i = i + 1
	elif(produto[p]=="M"):
		total = total+4.5
		m = m + 1
	elif(produto[p]=="S"):
		total = total+2.90
		s = s + 1
	p = p + 1
print(round(total,2), i, m, s)