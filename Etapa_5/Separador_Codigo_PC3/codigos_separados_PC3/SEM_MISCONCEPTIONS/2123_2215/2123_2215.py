from numpy import*

n=array(eval(input("nota:")))

media=(sum(n) - min(n))/3.0

if(media>=5):

	mensagem="APROVOU".upper()
else:
	mensagem="REPROVOU".upper()

print(round(media,2))
print(mensagem)