from numpy import*

t = array(eval(input("Tempos: ")))


i = 0

while(i<size(t)):
	if(t[i] == min(t)):
		print(i)
	i = i + 1