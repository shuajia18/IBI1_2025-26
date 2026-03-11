#initial population
#growth rate
#the next day population
#count wich day
#terminal when population reaches 91
a=5 #initial population
b=1.4 #growth rate
n=1 #count wich day
while a<91: #terminal when population reaches 91
    n +=1
    a=a*b #population of next day
n=n+1
print(n)
n=11