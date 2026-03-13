# What does this piece of code do?
# Answer: randomly choose eleven numbers form (1,10), while numbers can be the same. count their sum

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0
progress=0
while progress<=10:
	progress+=1 #do the calculations ten times 
	n = randint(1,10)
	total_rand+=n #caulate the sum of random numbers

print(total_rand)

#answer:is that randomly choose eleven numbers form (1,10), while numbers can be the same. count their sum
#result:68 58 68 62 56 66 52
#hypotheis: the total_rand is near to 60.5
