m=float(input( ))
a=float(input( ))
r=float(input( ))
i=float(input( ))
f=float(input( ))

media=(m+a+r+i+f)/5
print(round(media, 2))

if media>=7 :
	print("Aprovacao")
else:
	print("Reprovacao por nota")