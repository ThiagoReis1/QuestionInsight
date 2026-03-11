from numpy import*

lista=
lista2=array(str(input()))
q=0
for s3 in range (0, size(lista)):
	if(lista[s3]!=',' or lista [s3]!='"' or lista [s3]!='['or lista [s3]!=']'):
		lista2[q]=lista[s3]
	if(lista[s3]==','):
		q=q+1

pala=input()
ind=-1

for s2 in range(0,size(palavra)):
	if (pala[s2]=='R'):
		pala[s2]='L'

for s1 in range(0,size(lista2)):
	if (pala==lista2[s1]):
		ind=s1
if (ind<0):
	print("NAO ENCONTRADA")
else:
	print(ind)