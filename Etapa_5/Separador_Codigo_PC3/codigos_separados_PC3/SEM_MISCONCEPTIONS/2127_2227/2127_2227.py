from numpy import*
notas=array(eval(input("digite medias: ")))
media=(sum(notas)-min(notas))/3

if(media>=50):
	print (round(media,2))
	print("APROVADO")
else:
	print (round(media,2))
	print("REPROVADO")