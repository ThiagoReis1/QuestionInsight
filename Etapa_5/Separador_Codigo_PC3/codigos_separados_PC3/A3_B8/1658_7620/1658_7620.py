from numpy import*

a=input('Digite os paises:').upper().split(',')

china=0
japao=0
coreia=0
mongolia=0
tail=0
pessoas=0
for i in range(len(a)):
	if(a[i]=='CHN'):
		china=china+1
	elif(a[i]=='JPN'):
		japao=japao+1
	elif(a[i]=='KOR'):
		coreia=coreia+1
	elif(a[i]=='MGL'):
		mongolia=mongolia+1
	elif(a[i]=='THA'):
		tail=tail+1
		
nb=array([china,japao,coreia,mongolia,tail])

print(max(nb))
print(nb)
		
	








