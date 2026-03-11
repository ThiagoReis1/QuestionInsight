from numpy import *

num = array(eval(input('Digite: ')))
peso = array([5,4,3,2])

media = num*peso
media = sum(num*peso)/sum(peso)
					  
print (round(media,2))

