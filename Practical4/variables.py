#2004 population
a=5.08

#2014 population
b=5.33

#2024 population
c=5.55

d=b-a
e=c-b

print("d=",d)
print("e=",e)
if d>e:
    print("d>e")
elif d==e :
    print("d=e")
else :
    print(d<e)

d= 0.25
e= 0.21999999999999975
d>e
#population	growth	is	decelerating

X = True
Y = False
W = X or Y
print(W)

X = True
Y = True
W = X or Y
print(W)

X = False
Y = True
W = X or Y
print(W)

X = False
Y = False
W = X or Y
print(W)

#W (X or Y) truth table：
#| X     | Y     | W (X or Y) |
#|-------|-------|------------|
#| True  | True  | True       |
#| True  | False | True       |
#| False | True  | True       |
#| False | False | False      |