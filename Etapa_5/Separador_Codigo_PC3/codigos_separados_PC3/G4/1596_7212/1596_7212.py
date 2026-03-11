from numpy import*

v = array(eval(input()))

sm = sum(v)

mf = sm - min(v)

media = (mf / (size(v)-1))

print(round(media,2))