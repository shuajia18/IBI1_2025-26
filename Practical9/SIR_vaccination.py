#copy codes from SIR.py
# #import necessary libraries
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm
#define variables of the model
N= 10000 #define the total number of people in the population
vaccination_rates=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0] #define vaccination rates
b= 0.3 #define for beta
g=0.05 #define for gamma
plt.figure(figsize=(6,4),dpi=150) #set up dimensions and resolution
for rate in vaccination_rates:
    V=int(N*rate)
    I= 1 #define people who are infected
    R= V #redefine people who are recoverd
    S= N-I-R #redefine people who are susceptible
    I_history=[I] #make teh list to track
#repeat for 1000 times
#caculate probability of getting infected
#determine who can get infected
#determine who can get recovered
#count for each type
#write the results into list for track
#creat list to track 
    for t in range(1001): #repeat for 1000 times
        p_infected= b*(I/N) #caculate probability of getting infected
        if S<0: #list the rate-1.0 condition separately
            S=0
            I=0
            R=N
            I_history=[I]
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
        I_history.append(I)
    
    #start drawing
    
    plt.plot(I_history,label=str(int(rate*100))+'%',color=cm.viridis(rate))
#set labels
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig('SIR_model_with_different_vaccination_rates.png')
#I think the herd immunity thershold may be around 80% for this particular disease