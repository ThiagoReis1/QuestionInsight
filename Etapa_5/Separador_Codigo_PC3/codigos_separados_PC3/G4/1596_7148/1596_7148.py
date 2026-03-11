from numpy import*

n = array(eval(input("")))
print(round((sum(n) - min(n))/(size(n) - 1),2))