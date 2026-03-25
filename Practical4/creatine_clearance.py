#konw the age 
#know the weight
#know whether female or not
#creatine concentration
#check whether variables in normal range
#how to make calculate
#give the result

a=1 #konw the age 
b=49 #know the weight
c=40 #creatine concentration
d=0
gender="female"
if a>100:
    d=1
    print('age variable needs to be corrected')#tell age variable needs corrected
if b<=20 or b>=80:
    d=1
    print('weight variable needs to be corrected')#tell weight variable needs corrected
if c<=0 or c>=100:
    d=1
    print('creatine concentration variable needs to be corrected')#tell creatine concentration needs corrected
if d==0:
    if gender=="female":
        e=(140-a)*b*0.85/(72*c) #how to make calculate
    else:
        e=(140-a)*b/(72*c) #how to make calculate
        print(e) #give the result
        #answer is 2.010190972222222
else:
    print('the variables do not meet requirement')


