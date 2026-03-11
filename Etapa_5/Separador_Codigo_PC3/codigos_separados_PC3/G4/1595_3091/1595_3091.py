from numpy import*
v=array(eval(input("")))
v1=min(v)
i=0
nota=0


while i<size(v):
	if v[i] != v1:
		nota=nota+(v[i])
	i=1+i
	
media=(nota)/(size(v)-1)

	
print(round(media, 2))