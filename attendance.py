#!/usr/bin/bash

# import OS module
import os
import sys
import pandas as pd
import csv

# Get the path
#path = "/home/almog/Desktop/test2/participant.csv"
path = sys.argv[1]
    
# If the path does not exist
if not os.path.isfile(path):
    print("This is not a path")
    sys.exit(1)
# If there is a second path
if len(sys.argv) != 2:
    sys.exit("Please run the 1 path only again")

#read a file        
df = pd.read_csv(path,encoding='utf-16',sep='\t',header=0)
#Create a new df
df2 = df[['Attendee Email','Name','Join Time','Leave Time','Attendance Duration']]
df2 = df2.sort_values('Join Time' and 'Leave Time' and 'Attendee Email').reset_index(drop=True)
#Changing title names and new df
df3 = df2.rename(index=str,columns={"Attendee Email": "Email",
                                    "Name": "Name",
                                    "Join Time": "Starting_time",
                                    "Leave Time": "Ending_time",
                                    "Attendance Duration":"Total_hours" })
#Eliminating background noise
df3['Starting_time'] = df3['Starting_time'].replace({'=':''}, regex=True)
df3['Ending_time'] = df3['Ending_time'].replace({'=':''}, regex=True)
df3['Total_hours'] = df3['Total_hours'].replace({'mins':''}, regex=True)
# df_new is for only results
data = {'Email': [], 'Name': [], 'total_time(mins)': []}
df_new = pd.DataFrame(data)

#check time overlap
def check_time_overlap(start_time1, end_time1, start_time2, end_time2):
    if (start_time1 <= end_time2) and (start_time2 < end_time1): 
        return True #true: overlap
    else:
        return False  #false not overlap
        
# Last arrangement and going over a rule df to new df    
for i in range(df3.shape[0]):
    # For printing the second column
    #If the lines of the email field are the same
    if df3.iloc[i,0] == 'NaN':
        break
    if  len(df3) != i+1 and df3.iloc[i,0] != df3.iloc[i+1,0]:
        df_new.loc[i,'Email'] = df3.iloc[i,0]
        df_new.loc[i,'Name'] = df3.iloc[i,1]
        df_new.loc[i,'total_time(mins)'] = df3.iloc[i,4] + 'mins'
    if len(df3) != i+1 and df3.iloc[i, 0] == df3.iloc[i+1, 0]:
        check_time = check_time_overlap(df3.iloc[i, 2],df3.iloc[i, 3],df3.iloc[i+1, 2],df3.iloc[i+1, 3])
        #Is there an overlap between the times?
        if check_time == False:
            df3.loc[i,'Total_hours'] = (df3.iloc[i, 4] + df3.iloc[i+1, 4])
        if check_time == True:
            max_num = max(int(df3.iloc[i,4]),int(df3.iloc[i+1,4]))
            df3.loc[i,'Total_hours'] = max_num
        i += 1

#printing the new df
print(df_new)








