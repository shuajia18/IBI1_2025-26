#initial population
#growth rate
#the next day population
#count which day
#terminal when population reaches 91
a=5 #initial population
b=1.4 #growth rate
n=1 #count which day
while a< 91: #terminal when n reaches 91
    print(f'the number of infected students for Day n is {int(a)}')
    n +=1
    a=a*b #population of next day
    
print(f'At Day {n}, all students are infected')
#n=10