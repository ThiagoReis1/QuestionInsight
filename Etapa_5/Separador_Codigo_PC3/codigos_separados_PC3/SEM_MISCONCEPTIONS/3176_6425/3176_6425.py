from numpy import*
st=input("palavra: ").lower()

vogais = array(["a","e","i","o","u"])
contv = 0
contc = 0

for i in st:
	if i in vogais:
		contv+=1
	else:
		contc+=1
		
print(contv)
print(contc)

	