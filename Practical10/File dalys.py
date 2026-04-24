#import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#change working directory to where download file exists
os.chdir('C:/Users/shuaj/Desktop/IBI/practical 3/IBI1_2025-26/Practical10')
print(os.getcwd()) #check where i am
print(os.listdir()) #list files under this folder

#read the content of .csv files into a dataframe object and call this dataframe dalys_data
dalys_data = pd.read_csv('dalys-rate-from-all-causes.csv')
print(dalys_data.head(5)) #see and print the content of first 5 rows
dalys_data.info() #get types of data points, colunmns' name and the number of rows
print(dalys_data.describe()) #analyze numbers

print(dalys_data.iloc[0,3])#show the value in the first row, fourth column
print(dalys_data.head(4))#print the first 4 row to check 

print(dalys_data.iloc[2,0:5]) #print the content of third row and column of first to fifth with their title
print(dalys_data.iloc[0:2,:]) #print the content of the first and second row
print(dalys_data.iloc[0:10:2,0:5]) #print the content of first to theth row, and divided by 2, and from the first column to fifth column

print(dalys_data.iloc[0:10,2:4]) #print the third and fourth columns for the first 10 rows
the_first_ten_rows=dalys_data.iloc[0:10,2:4]  #get the third and fourth columns for the first 10 rows
print('The year reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistanthe is 1998') #report the maximum year


print(dalys_data.iloc[0:3,[0,1,3]])
my_columns=[True,True,False,True]
print(dalys_data.iloc[0:3,my_columns])
#If  my_columns is shorter or longer than the number of columns of your data frame, the system would report errors

print(dalys_data.loc[2:4,'Year']) #print the third to fourth row in the column of Year

my_rows=[]
all_rows=dalys_data.loc[:,'Year']
for i in range(len(all_rows)):
    if dalys_data.loc[i,'Entity'] == 'Zimbabwe':
        my_rows.append(True)
    else:
        my_rows.append(False)
specific_rows=all_rows.iloc[my_rows]
print(specific_rows)
first_year=specific_rows.iloc[0]
last_year=specific_rows.iloc[-1]
print(f'The first year these data were recorded is {first_year}')
print(f'The last year these data were recorded is {last_year}')

#answer the question: What country or countries have recorded a DALYs less than 18,000 in a single year?
question_frame=dalys_data.loc[:,['Entity','DALYs']]
row_number_of_queation_frame=len(question_frame)
countries=[]
for i in range(row_number_of_queation_frame):
    if question_frame.iloc[i,1] <18000:
        got_country=dalys_data.iloc[i,0]
        if got_country in countries:
            countries=countries
        else:
            countries.append(got_country)
print(f'{countries} have recorded a DALYs less than 18,000 in a single year')



recent_data= dalys_data.loc[dalys_data.Year ==2019,['Entity','DALYs']] #get spearate dataframe for year of 2019 and required columns
row_number= len(recent_data)
largest_DALYs=recent_data.iloc[0,1] #here should not use loc but need to use iloc, iloc[i] is actually researching for i row in the new frame. But loc[i] is still researching for i row at past dataframe
largest_country=recent_data.iloc[0,0]
smallest_DALYs=recent_data.iloc[0,1]
smallest_country=recent_data.iloc[0,0]
for i in range(row_number):
    DALYs= recent_data.iloc[i,1]
    country= recent_data.iloc[i,0]
    if DALYs >= largest_DALYs:
        largest_DALYs=DALYs
        largest_country=country
    if DALYs <=smallest_DALYs:
        smallest_DALYs= DALYs
        smallest_country=country
print(f'The largest DALYs is {largest_DALYs}, the corresponding country is {largest_country}')
print(f'The smallest DALYs is {smallest_DALYs}, the corresponding country is {smallest_country}')

Singapore = dalys_data.loc[dalys_data.Entity == 'Singapore']
plt.plot(Singapore.Year,Singapore.DALYs,'bo-') #b+ shows the image in blue and +, r+ shows the image in red and +, bo shows the image in blue and o
#b/r indicates the colour, o/-/+ shows the shape
plt.xticks(Singapore.Year,rotation=45) #tell system to show all the years,change the rotation angle and can show the xsticks clearer
plt.xlabel('Year')
plt.ylabel('The total DALYs')
plt.title('The DALYs over years in Singapore')
plt.show()
