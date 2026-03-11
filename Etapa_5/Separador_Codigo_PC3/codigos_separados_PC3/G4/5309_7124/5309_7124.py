x= float (input("numero real:"))
k= int(input("numero inteiro:"))
imp= 1
cont= 1
soma= 0

while(cont<=k):
	soma= soma + (x/imp)
	imp= imp+2
	cont= cont+1
	
print (round(soma,8))