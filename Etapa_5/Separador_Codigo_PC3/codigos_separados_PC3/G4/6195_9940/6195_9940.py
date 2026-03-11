n= int(input())
tx= int(input())
cont=0
q=n
while q<(n*2):
	q=q+q*(tx/100)
	cont=cont+1
print(cont)
