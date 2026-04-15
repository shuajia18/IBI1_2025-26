#import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt
#define variables of the model
N= 10000 #define the total number of people in the population
I= 1 #define people who are infected
S= N-I #define people who are susceptible
R= 0 #define people who are recoverd

b= 0.3 #define for beta
g=0.05 #define for gamma
#creat list to track 
S_history= [S]
I_history= [I]
R_history= [R]
#repeat for 1000 times
#caculate probability of getting infected
#determine who can get infected
#determine who can get recovered
#count for each type
#write the results into list for track
for t in range(1001): #repeat for 1000 times
    p_infected= b*(I/N) #caculate probability of getting infected
    infected= np.random.choice(range(2),size=S,p=[1-p_infected,p_infected]) #count 1 as infected
    new_infected= 0
    for people in infected:
        if people ==1:
            new_infected +=1

    recovered =np.random.choice(range(2),I,p=[1-g,g])
    new_recovered= 0
    for people in recovered:
        if people ==1:
            new_recovered +=1
    S= S-new_infected
    I= I+new_infected-new_recovered
    R= R+new_recovered
    S_history.append(S)
    I_history.append(I)
    R_history.append(R)
#start drawing
plt.figure(figsize=(6,4),dpi=150) #set up dimensions and resolution
plt.plot(S_history,label='susceptible',color='blue')
plt.plot(I_history,label='infected',color='orange')
plt.plot(R_history,label='recovered',color='green')
#set labels
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.savefig('SIR_model.png')
#If i run it for several times, the resulting images are also different, and the differences are also big. If i change gamma for smaller, the recovered population would reach 10000 later. And if i change beta for larger, the highest value of infected pople can get larger 

