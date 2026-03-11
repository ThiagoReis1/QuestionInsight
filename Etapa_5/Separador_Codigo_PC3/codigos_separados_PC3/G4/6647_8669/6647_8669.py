from numpy import*
peso= array([2,1,5])
nota= array(eval(input("insira a nota: ")))
num= sum(peso*nota)
den= sum(peso)
media= num/den
print(round(media,2))
