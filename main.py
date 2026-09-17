"""READ DATA """

import pandas as pd

#read data 

df=pd.read_csv('youtube_dataset.csv')
#print(df)

#UNDERSTANDIN DATA 

# print(df.info())
# #print(df.describe())
#   print(df.isnull())
# print(df.head(10))

#ESTIMETED VALUES FILLING

df["Views"]=df['Views'].interpolate(method="linear",inplace=True)
df['Videos']=df['Videos'].interpolate(method='linear',inplace=True)
df['Watch_Time']=df['Watch_Time'].interpolate(method='linear',inplace=True)
# print(df)
# print(df.isnull())


"""ACTUAL ANALYSIS"""

sprted_data=df.sort_values(by=['Views','Channel_Name'],ascending=[False,True])  # HIGHEST VIEWS CAHNNEL=MUSIC BEAT
# print(sprted_data)
# print(df['Channel_Name'].count())  #25 CAHNNELS ARE THERE

opration_new=df.sort_values(by=['Revenue'],ascending=False)
# print(opration_new.head())#13    MusicBeat       280000  8100000.0   350.0   1100000.0    75000,


opration_2=df.sort_values(by=['Revenue'],ascending=False)
print(opration_2)   # IN ALL TOTAL OPERATION 

high_revenue=df[df['Revenue']>40000]
print(high_revenue)

# creating columns 
df['Revenue_Status']="Normal"
df.loc[df['Revenue']>40000,"Revenue_Status"]="High"    
print(df)

df.to_excel('Cleand_yt_analysis.xlsx',index=False)

print("Succesfully Retrived data cleainig")