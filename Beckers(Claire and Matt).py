# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

repository:
    /Users/arthurmendes/Desktop/Marketing Analysis
"""

import pandas as pd


# Import Salesforce dataset
SF_1 = pd.read_excel('Beckers - Claire and Matt.xls')

SF_1.head()

# Import HubSpot Dataset
HS_1 = pd.read_csv(
        'hubspot-digest-email-events-basic-recipients-list-2019-07-23.csv')

HS_1.head()

# Merge datasets on "Email"
df_merge_col = pd.merge(SF_1, HS_1, on='Email')

df_merge_col.columns

# Create a function to count the number of accounts on each sales representative

def appcount(df, col, x):
    return (df[col] == x).sum()

# use App count

df_merge_col['Territory Owner'].unique()

#### 'Claire Stovall'
# Count of number of countacts
Number_Contact_Claire = appcount(
        df_merge_col, 'Territory Owner','Claire Stovall')

# Email Sent
Emails_Sent_Claire = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Claire Stovall' , ['Sent']].sum()

SentPofCont = Emails_Sent_Claire/Number_Contact_Claire

# Emails Open
Emails_Opened_Claire = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Claire Stovall', ['Opened']].sum()

OpenedPofSent = Emails_Opened_Claire/Emails_Sent_Claire[0]

# Numbers of Clicks
Clicks_Claire = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Claire Stovall', ['Clicked']].sum()

ClicksPofOpened = Clicks_Claire/Emails_Opened_Claire[0]

# NUmber of registrantants

Regis_Claire = 37

ClicksPofOpened = Regis_Claire/Emails_Opened_Claire[0]

# Claire clicked

Ccliked = df_merge_col[(df_merge_col['Territory Owner'] == 'Claire Stovall') & (df_merge_col['Clicked'] == 'True')]

# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Claire Stovall'

ClaireData = df_merge_col.loc[selected_sp]

selectedEmailStatus = ClaireData['Clicked'] == True

ClaireClicked =ClaireData.loc[selectedEmailStatus]

"""
# Save as a excel file
ClaireClicked.to_excel('ClaireClicked.xlsx')
"""

# Counting the tittles
Who_Clicked_Claire = ClaireClicked['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Clicked_Claire.to_excel('Who Clicked Claire.xlsx')
"""

#######################
# Selecting the people that opened 

selectedEmailStatus = ClaireData['Opened'] == True

ClaireOpened = ClaireData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Claire = ClaireOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Claire.to_excel('Who Opened Claire.xlsx')
"""



"""
df_merge_col[['Territory Owner']].count().sum().where(
        df_merge_col['Sentt'] == 'True')

"""


# 'Matt Parrack'

appcount(df_merge_col, 'Territory Owner', 'Matt Parrack')

#### 'Matt Parrack'
# Count of number of countacts
Number_Contact_Matt = appcount(
        df_merge_col, 'Territory Owner','Matt Parrack')

# Email Sent
Emails_Sent_Matt = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Matt Parrack', ['Sent']].sum()

SentPofCont_M = Emails_Sent_Matt/Number_Contact_Matt

# Emails Open
Emails_Opened_Matt = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Matt Parrack', ['Opened']].sum()

OpenedPofSent_M = Emails_Opened_Matt/Emails_Sent_Matt[0]

# Numbers of Clicks
Clicks_Matt = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Matt Parrack', ['Clicked']].sum()

ClicksPofOpened_M = Clicks_Matt/Emails_Opened_Matt[0]

# NUmber of registrantants

Regis_Matt = 11

ClicksPofOpened = Regis_Matt/Emails_Opened_Matt[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Matt Parrack'

MattData = df_merge_col.loc[selected_sp]

selectedEmailStatus = MattData['Clicked'] == True

MatttClicked = MattData.loc[selectedEmailStatus]

MatttClicked.to_excel('MatttClicked.xlsx')

# Who Clicked
Who_Clicked_Matt = MatttClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_Matt.to_excel('Who Clicked Matt.xlsx')

"""



#######################
# Selecting the people that opened 

selectedEmailStatus = MattData['Opened'] == True

MattOpened = MattData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Matt = MattOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Matt.to_excel('Who Opened Matt.xlsx')
"""

