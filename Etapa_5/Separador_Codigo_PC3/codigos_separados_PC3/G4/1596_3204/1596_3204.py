from numpy import*

v = array(eval(input()))

	
h=sum(v)-min(v)
x = h/(size(v)-1)




print(round(x,2))