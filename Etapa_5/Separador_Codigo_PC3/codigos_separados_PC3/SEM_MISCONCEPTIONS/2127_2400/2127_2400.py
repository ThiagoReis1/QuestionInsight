from numpy import*

nota=array(eval(input()))
lol=min(nota)
media=(sum(nota)-lol)/(size(nota)-1)
print(round(media,2))
if(media>=50):
	print("APROVADO")
else:
	print("REPROVADO")