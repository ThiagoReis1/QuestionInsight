from numpy import*
n = array(eval(input("notas do trabalho ")))
i = 0
if(n[i] == min(n)):
	   s = sum(n) - n[i]
	   v = size(n) - 1 else:
		s = sum(n)
		v = size(n)
		i = i + 1
   media = s/v
print(round(media, 2))