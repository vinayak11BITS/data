import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#loading the dataframe of the company
df=pd.read_csv("C:\\Users\\vinayak\\Downloads\\edureka\\BigMartSalesData.csv")
print(df)#printing the total dataframe

df_n=df[['Amount','Year','Month']]#sub dividing the dataframe into three columns
print(df_n)#printing the new dataframe

df_n1=df_n[df_n['Year']==2011]#only considering year 2011 for analysis
print(df_n1)#printing the new dataframe containing details of year 2011

#sub dividing the above data frame into many new data frames acc. to months
df_n12=df_n1[df_n1['Month']==12]#considering the month 
print(df_n12)#printing the monthly dataframe
x_12=df_n12['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n11=df_n1[df_n1['Month']==11]#considering the month 
print(df_n11)#printing the monthly dataframe
x_11=df_n11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n10=df_n1[df_n1['Month']==10]#considering the month
print(df_n10)#printing the monthly dataframe
x_10=df_n10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n9=df_n1[df_n1['Month']==9]#considering the month
print(df_n9)#printing the monthly dataframe
x_9=df_n9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n8=df_n1[df_n1['Month']==8]#considering the month
print(df_n8)#printing the monthly dataframe
x_8=df_n8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n7=df_n1[df_n1['Month']==7]#considering the month
print(df_n7)#printing the monthly dataframe
x_7=df_n7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n6=df_n1[df_n1['Month']==6]#considering the month
print(df_n6)#printing the monthly dataframe
x_6=df_n6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n5=df_n1[df_n1['Month']==5]#considering the month
print(df_n5)#printing the monthly dataframe
x_5=df_n5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n4=df_n1[df_n1['Month']==4]#considering the month
print(df_n4)#printing the monthly dataframe
x_4=df_n4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n3=df_n1[df_n1['Month']==3]#considering the month
print(df_n3)#printing the monthly dataframe
x_3=df_n3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n2=df_n1[df_n1['Month']==2]#considering the month
print(df_n2)#printing the monthly dataframe
x_2=df_n2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_n1=df_n1[df_n1['Month']==1]#considering the month
print(df_n1)#printing the monthly dataframe
x_1=df_n1['Amount'].sum(axis=0)#taking sum of all rows of that month

#creating an enitrely new dataframe which has all monthly data
data={'Month':[1,2,3,4,5,6,7,8,9,10,11,12],'Amount':[x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10,x_11,x_12]}
df_new = pd.DataFrame (data, columns = ['Month','Amount'])
print(df_new)
#plotting the bar graph of monthly amount of 2011
sns.barplot(y=df_new['Amount'],x=df_new['Month'])
#plotting the line graph of montly amount of 2011
df_new.plot()
#plotting the pie chart of montly amount of yer 2011
df_new.plot.pie(y='Amount',figsize=(5,5))

df_nc=df[['Amount','Year','Month','Country']]
print(df_nc)


df_nc1=df_nc[df_nc['Year']==2011]#only considering year 2011 for analysis
print(df_nc1)

#######CALCULATING THE NUMBER OF COUNTRIES######

lst=df_nc1['Country'].values

newstr=list(lst) #creating a new list using string
newlist=[]
for index in newstr:
    if index not in newlist:
        newlist.append(index)
        count=0
        for _ in range(len(newstr)):
            if index==newstr[_]:
                count+=1
        print("{},{}".format(index,count))   
    
##################################################
##################################################
####FOR UNITED KINGDOM#######
df_nc2=df_nc1[df_nc1['Country']=='United Kingdom']
print(df_nc2)

#sub dividing the above data frame into many new data frames acc. to months
df_nc12=df_nc2[df_nc2['Month']==12]#considering the month 
print(df_nc12)#printing the monthly dataframe
x_c12=df_nc12['Amount'].sum(axis=0)#taking sum of all rows of that month

df_nc11=df_nc2[df_nc2['Month']==11]#considering the month 
print(df_nc11)#printing the monthly dataframe
x_c11=df_nc11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc10=df_nc2[df_nc2['Month']==10]#considering the month
print(df_nc10)#printing the monthly dataframe
x_c10=df_nc10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc9=df_nc2[df_nc2['Month']==9]#considering the month
print(df_nc9)#printing the monthly dataframe
x_c9=df_nc9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc8=df_nc2[df_nc2['Month']==8]#considering the month
print(df_nc8)#printing the monthly dataframe
x_c8=df_nc8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc7=df_nc2[df_nc2['Month']==7]#considering the month
print(df_nc7)#printing the monthly dataframe
x_c7=df_nc7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc6=df_nc2[df_nc2['Month']==6]#considering the month
print(df_nc6)#printing the monthly dataframe
x_c6=df_nc6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc5=df_nc2[df_nc2['Month']==5]#considering the month
print(df_nc5)#printing the monthly dataframe
x_c5=df_nc5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc4=df_nc2[df_nc2['Month']==4]#considering the month
print(df_nc4)#printing the monthly dataframe
x_c4=df_nc4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nc3=df_nc2[df_nc2['Month']==3]#considering the month
print(df_nc3)#printing the monthly dataframe
x_c3=df_nc3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncc2=df_nc2[df_nc2['Month']==2]#considering the month
print(df_ncc2)#printing the monthly dataframe
x_c2=df_ncc2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncc1=df_nc2[df_nc2['Month']==1]#considering the month
print(df_ncc1)#printing the monthly dataframe
x_c1=df_ncc1['Amount'].sum(axis=0)#taking sum of all rows of that month

x_ct_uk=x_c1+x_c2+x_c3+x_c4+x_c5+x_c6+x_c7+x_c8+x_c9+x_c10+x_c11+x_c12
print(x_ct_uk)

#############################################################
####FOR SWEDEN######################
df_ncs2=df_nc1[df_nc1['Country']=='Sweden']
print(df_ncs2)

#sub dividing the above data frame into many new data frames acc. to months
df_ncs12=df_ncs2[df_ncs2['Month']==12]#considering the month 
print(df_ncs12)#printing the monthly dataframe
x_cs12=df_ncs12['Amount'].sum(axis=0)#taking sum of all rows of that month

df_ncs11=df_ncs2[df_ncs2['Month']==11]#considering the month 
print(df_ncs11)#printing the monthly dataframe
x_cs11=df_ncs11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs10=df_ncs2[df_ncs2['Month']==10]#considering the month
print(df_ncs10)#printing the monthly dataframe
x_cs10=df_ncs10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs9=df_ncs2[df_ncs2['Month']==9]#considering the month
print(df_ncs9)#printing the monthly dataframe
x_cs9=df_ncs9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs8=df_ncs2[df_ncs2['Month']==8]#considering the month
print(df_ncs8)#printing the monthly dataframe
x_cs8=df_ncs8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs7=df_ncs2[df_ncs2['Month']==7]#considering the month
print(df_ncs7)#printing the monthly dataframe
x_cs7=df_ncs7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs6=df_ncs2[df_ncs2['Month']==6]#considering the month
print(df_ncs6)#printing the monthly dataframe
x_cs6=df_ncs6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs5=df_ncs2[df_ncs2['Month']==5]#considering the month
print(df_ncs5)#printing the monthly dataframe
x_cs5=df_ncs5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs4=df_ncs2[df_ncs2['Month']==4]#considering the month
print(df_ncs4)#printing the monthly dataframe
x_cs4=df_ncs4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncs3=df_ncs2[df_ncs2['Month']==3]#considering the month
print(df_ncs3)#printing the monthly dataframe
x_cs3=df_ncs3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccs2=df_ncs2[df_ncs2['Month']==2]#considering the month
print(df_nccs2)#printing the monthly dataframe
x_ccs2=df_nccs2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccs1=df_ncs2[df_ncs2['Month']==1]#considering the month
print(df_nccs1)#printing the monthly dataframe
x_ccs1=df_nccs1['Amount'].sum(axis=0)#taking sum of all rows of that month

x_ct_s=x_ccs1+x_ccs2+x_cs3+x_cs4+x_cs5+x_cs6+x_cs7+x_cs8+x_cs9+x_cs10+x_cs11+x_cs12
print(x_ct_s)

##################################################
####FOR ITALY#######
df_nc2=df_nc1[df_nc1['Country']=='Italy']
print(df_nc2)

#sub dividing the above data frame into many new data frames acc. to months
df_nci12=df_nc2[df_nc2['Month']==12]#considering the month 
print(df_nci12)#printing the monthly dataframe
x_ci12=df_nci12['Amount'].sum(axis=0)#taking sum of all rows of that month

df_nci11=df_nc2[df_nc2['Month']==11]#considering the month 
print(df_nci11)#printing the monthly dataframe
x_ci11=df_nci11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci10=df_nc2[df_nc2['Month']==10]#considering the month
print(df_nci10)#printing the monthly dataframe
x_ci10=df_nci10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci9=df_nc2[df_nc2['Month']==9]#considering the month
print(df_nci9)#printing the monthly dataframe
x_ci9=df_nci9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci8=df_nc2[df_nc2['Month']==8]#considering the month
print(df_nci8)#printing the monthly dataframe
x_ci8=df_nci8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci7=df_nc2[df_nc2['Month']==7]#considering the month
print(df_nci7)#printing the monthly dataframe
x_ci7=df_nci7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci6=df_nc2[df_nc2['Month']==6]#considering the month
print(df_nci6)#printing the monthly dataframe
x_ci6=df_nci6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci5=df_nc2[df_nc2['Month']==5]#considering the month
print(df_nci5)#printing the monthly dataframe
x_ci5=df_nci5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci4=df_nc2[df_nc2['Month']==4]#considering the month
print(df_nci4)#printing the monthly dataframe
x_ci4=df_nci4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nci3=df_nc2[df_nc2['Month']==3]#considering the month
print(df_nci3)#printing the monthly dataframe
x_ci3=df_nci3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncci2=df_nc2[df_nc2['Month']==2]#considering the month
print(df_ncci2)#printing the monthly dataframe
x_ci2=df_ncci2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncci1=df_nc2[df_nc2['Month']==1]#considering the month
print(df_ncci1)#printing the monthly dataframe
x_ci1=df_ncci1['Amount'].sum(axis=0)#taking sum of all rows of that month

x_ct_i=x_ci1+x_ci2+x_ci3+x_ci4+x_ci5+x_ci6+x_ci7+x_ci8+x_ci9+x_ci10+x_ci11+x_ci12
print(x_ct_i)


##################################################
####FOR PORTUGAL#######
df_nc2=df_nc1[df_nc1['Country']=='Portugal']
print(df_nc2)

#sub dividing the above data frame into many new data frames acc. to months
df_ncp12=df_nc2[df_nc2['Month']==12]#considering the month 
print(df_ncp12)#printing the monthly dataframe
x_cp12=df_ncp12['Amount'].sum(axis=0)#taking sum of all rows of that month

df_ncp11=df_nc2[df_nc2['Month']==11]#considering the month 
print(df_ncp11)#printing the monthly dataframe
x_cp11=df_ncp11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp10=df_nc2[df_nc2['Month']==10]#considering the month
print(df_ncp10)#printing the monthly dataframe
x_cp10=df_ncp10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp9=df_nc2[df_nc2['Month']==9]#considering the month
print(df_ncp9)#printing the monthly dataframe
x_cp9=df_ncp9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp8=df_nc2[df_nc2['Month']==8]#considering the month
print(df_ncp8)#printing the monthly dataframe
x_cp8=df_ncp8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp7=df_nc2[df_nc2['Month']==7]#considering the month
print(df_ncp7)#printing the monthly dataframe
x_cp7=df_ncp7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp6=df_nc2[df_nc2['Month']==6]#considering the month
print(df_ncp6)#printing the monthly dataframe
x_cp6=df_ncp6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp5=df_nc2[df_nc2['Month']==5]#considering the month
print(df_ncp5)#printing the monthly dataframe
x_cp5=df_ncp5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp4=df_nc2[df_nc2['Month']==4]#considering the month
print(df_ncp4)#printing the monthly dataframe
x_cp4=df_ncp4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncp3=df_nc2[df_nc2['Month']==3]#considering the month
print(df_ncp3)#printing the monthly dataframe
x_cp3=df_ncp3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccp2=df_nc2[df_nc2['Month']==2]#considering the month
print(df_nccp2)#printing the monthly dataframe
x_cp2=df_nccp2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccp1=df_nc2[df_nc2['Month']==1]#considering the month
print(df_nccp1)#printing the monthly dataframe
x_cp1=df_nccp1['Amount'].sum(axis=0)#taking sum of all rows of that month

x_ct_p=x_cp1+x_cp2+x_cp3+x_cp4+x_cp5+x_cp6+x_cp7+x_cp8+x_cp9+x_cp10+x_cp11+x_cp12
print(x_ct_p)

#############################################################
#######FOR FRANCE##############

df_nc2=df_nc1[df_nc1['Country']=='France']
print(df_nc2)

#sub dividing the above data frame into many new data frames acc. to months
df_ncf12=df_nc2[df_nc2['Month']==12]#considering the month 
print(df_ncf12)#printing the monthly dataframe
x_cf12=df_ncf12['Amount'].sum(axis=0)#taking sum of all rows of that month

df_ncf11=df_nc2[df_nc2['Month']==11]#considering the month 
print(df_ncf11)#printing the monthly dataframe
x_cf11=df_ncf11['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf10=df_nc2[df_nc2['Month']==10]#considering the month
print(df_ncf10)#printing the monthly dataframe
x_cf10=df_ncf10['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf9=df_nc2[df_nc2['Month']==9]#considering the month
print(df_ncf9)#printing the monthly dataframe
x_cf9=df_ncf9['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf8=df_nc2[df_nc2['Month']==8]#considering the month
print(df_ncf8)#printing the monthly dataframe
x_cf8=df_ncf8['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf7=df_nc2[df_nc2['Month']==7]#considering the month
print(df_ncf7)#printing the monthly dataframe
x_cf7=df_ncf7['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf6=df_nc2[df_nc2['Month']==6]#considering the month
print(df_ncf6)#printing the monthly dataframe
x_cf6=df_ncf6['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf5=df_nc2[df_nc2['Month']==5]#considering the month
print(df_ncf5)#printing the monthly dataframe
x_cf5=df_ncf5['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf4=df_nc2[df_nc2['Month']==4]#considering the month
print(df_ncf4)#printing the monthly dataframe
x_cf4=df_ncf4['Amount'].sum(axis=0)#taking sum of all rows of that month


df_ncf3=df_nc2[df_nc2['Month']==3]#considering the month
print(df_ncf3)#printing the monthly dataframe
x_cf3=df_ncf3['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccf2=df_nc2[df_nc2['Month']==2]#considering the month
print(df_nccf2)#printing the monthly dataframe
x_cf2=df_nccf2['Amount'].sum(axis=0)#taking sum of all rows of that month


df_nccf1=df_nc2[df_nc2['Month']==1]#considering the month
print(df_nccf1)#printing the monthly dataframe
x_cf1=df_nccf1['Amount'].sum(axis=0)#taking sum of all rows of that month

x_ct_f=x_cf1+x_cf2+x_cf3+x_cf4+x_cf5+x_cf6+x_cf7+x_cf8+x_cf9+x_cf10+x_cf11+x_cf12
print(x_ct_f)

#########################################################

x_ct_total=(x_ct_uk+x_ct_s+x_ct_i+x_ct_p+x_ct_f)
print(x_ct_total)


#creating an enitrely new dataframe which has all country data
data_c={'Country':['United Kingdom','Sweden','Italy','Portugal','France'],'Amount':[x_ct_uk,x_ct_s,x_ct_i,x_ct_p,x_ct_f]}
df_new_c = pd.DataFrame (data_c, columns = ['Country','Amount'])
print(df_new_c)
#plotting the bar graph of country amount of 2011
sns.barplot(y=df_new_c['Amount'],x=df_new_c['Country'])

###############################################################
##################################################################
################################################################



