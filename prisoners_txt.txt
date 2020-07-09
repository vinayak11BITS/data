##############################################
#############################################
#####CASE STUDY-1 MODULE-5###################

import pandas as pd#importing pandas to perform data analysis
import seaborn as sns#to visualize data
from matplotlib import pyplot as plt#to visualize data

#reading data from prisoners.csv file
df=pd.read_csv('C:\\Users\\vinayak\\Downloads\\D6_Sessions_practise\\prisoners.csv')
print(df)

#describing the dataframe
df.describe()
#checking if there is any null value in dataframe
df.isnull().sum()
df=df.dropna()#dropping the null values
print(df.isnull().sum())

#creating a new dataframe from existing 
dff=pd.DataFrame({'No. of Inmates benefitted by Elementary Education':df['No. of Inmates benefitted by Elementary Education'],'No. of Inmates benefitted by Adult Education':df['No. of Inmates benefitted by Adult Education'],'No. of Inmates benefitted by Higher Education':df['No. of Inmates benefitted by Higher Education'],'No. of Inmates benefitted by Computer Course':df['No. of Inmates benefitted by Computer Course'],'total_benefitted':df.sum(axis=1)})
print(dff)

#taking sum along each column
x1=df['No. of Inmates benefitted by Elementary Education'].sum(axis=0)
print(x1)
x2=df['No. of Inmates benefitted by Adult Education'].sum(axis=0)
print(x2)
x3=df['No. of Inmates benefitted by Higher Education'].sum(axis=0)
print(x3)
x4=df['No. of Inmates benefitted by Computer Course'].sum(axis=0)
print(x4)
#total of each column
xt=x1+x2+x3+x4
print(xt)
#adding a new colum to the above dataframe
data=[(x1,x2,x3,x4,xt)]
df_obj=pd.DataFrame(data,columns=['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education','No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course','total_benefitted'],index=['totals'])
print(df_obj)
#final dat frame having totals as row and total benefitted as new column
modDfobj=dff.append(df_obj, ignore_index=True)
print(modDfobj)
#plotting the bar graph between the state and total benefitted data
sns.barplot(x=df['STATE/UT'],y=dff['total_benefitted'])
# Data to plot
labels = 'No. of Inmates benefitted by Elementary Education', 'No. of Inmates benefitted by Adult Education', 'No. of Inmates benefitted by Higher Education', 'No. of Inmates benefitted by Computer Course'
sizes = [x1,x2,x3,x4]
# Plot
plt.pie(sizes, labels=labels)
plt.axis('equal')
plt.show()

