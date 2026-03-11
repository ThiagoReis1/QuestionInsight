from numpy import*

n = array(eval(input("notas:")))
print(round((sum(n)-min(n))/(size(n) -1) , 2))