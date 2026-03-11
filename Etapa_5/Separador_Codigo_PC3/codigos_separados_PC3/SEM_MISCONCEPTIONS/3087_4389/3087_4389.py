num =  int(input("Informe um numero: \n"))
i = 0
f = 0
media = 0
media2 = 0

while(num!=0):
	
	if(num%2==0):
		i = i + num
		media = media + 1
	
	else:
		f = f + num
		media2 = media2 + 1
	
	num = int(input("Informe um numero: \n"))
#a = round(i/media,2)
#b = round(f/media2,2)
#print(a)
#print(b)
if(i/media!=0)and(media2!=0):
	print(round(i/media,2))
	print(round(f/media2,2))

elif(media==0)and(f/media2!=0):
	print(0.0)
	print(round(f/media2,2))

else:
	print(round(i/media,2))
	print(0.0)