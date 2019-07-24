#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:26:45 2019

@author: arthurmendes

Directory: /Users/arthurmendes/Desktop/Beckers Analysis/Second_Email
"""


import pandas as pd


# Import Salesforce dataset
SF_1 = pd.read_csv('report1563909905865.csv')

SF_1.head()

# Import HubSpot Dataset
HS_1 = pd.read_csv('events.csv')

HS_1.head()

# Merge datasets on "Email"
df_merge_col = pd.merge(SF_1, HS_1, on='Email')

df_merge_col.columns


# Create a function to count the number of accounts on each sales representative

def appcount(df, col, x):
    return (df[col] == x).sum()

# Unique Territory Owners

df_merge_col['Territory Owner'].unique()


############################################
## Andrew Card'
############################################

# Count of number of countacts
Number_Contact_Andrew = appcount(
        df_merge_col, 'Territory Owner','Andrew Card')


# Email Sent
Emails_Sent_Andrew = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Andrew Card', ['Sent']].sum()

SentPofCont_A = Emails_Sent_Andrew/Number_Contact_Andrew

# Emails Open
Emails_Opened_Andrew = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Andrew Card', ['Opened']].sum()

OpenedPofSent_A = Emails_Opened_Andrew/Emails_Sent_Andrew[0]

# Numbers of Clicks
Clicks_Andrew = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Andrew Card', ['Clicked']].sum()

ClicksPofOpened_A = Clicks_Andrew/Emails_Opened_Andrew[0]

# NUmber of registrantants

Regis_Andrew = 20

ClicksPofOpened_A = Regis_Andrew/Emails_Opened_Andrew[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Andrew Card'

AndrewData = df_merge_col.loc[selected_sp]

selectedEmailStatus = AndrewData['Clicked'] == True

AndrewClicked = AndrewData.loc[selectedEmailStatus]

AndrewClicked.to_excel('AndrewClicked.xlsx')


# Who Clicked
Who_Clicked_Andrew = AndrewClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_Andrew.to_excel('Who Clicked Andrew.xlsx')

"""

#######################
# Selecting the people that opened 

selectedEmailStatus = AndrewData['Opened'] == True

AndrewOpened = AndrewData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Andrew = AndrewOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Andrew.to_excel('Who Opened Andrew.xlsx')
"""






############################################
## Brian Duffy
############################################

# Count of number of countacts
Number_Contact_Brian = appcount(
        df_merge_col, 'Territory Owner', 'Brian Duffy')


# Email Sent
Emails_Sent_Brian = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Brian Duffy', ['Sent']].sum()

SentPofCont_B = Emails_Sent_Brian/Number_Contact_Brian

# Emails Open
Emails_Opened_Brian = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Brian Duffy', ['Opened']].sum()

OpenedPofSent_B = Emails_Opened_Brian/Emails_Sent_Brian[0]

# Numbers of Clicks
Clicks_Brian = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Brian Duffy', ['Clicked']].sum()

ClicksPofOpened_B = Clicks_Brian/Emails_Opened_Brian[0]

# NUmber of registrantants

Regis_Brian = 45

ClicksPofOpened_B = Regis_Brian/Emails_Opened_Brian[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Brian Duffy'

BrianData = df_merge_col.loc[selected_sp]

selectedEmailStatus = BrianData['Clicked'] == True

BrianClicked = BrianData.loc[selectedEmailStatus]

BrianClicked.to_excel('BrianClicked.xlsx')


# Who Clicked
Who_Clicked_Brian = BrianClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_Brian.to_excel('Who Clicked Brian.xlsx')

"""

#######################
# Selecting the people that opened 

selectedEmailStatus = BrianData['Opened'] == True

BrianOpened = BrianData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Brian = BrianOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Brian.to_excel('Who Opened Brian.xlsx')
"""


############################################
## Josh Macy
############################################

# Count of number of countacts
Number_Contact_JoshM = appcount(
        df_merge_col, 'Territory Owner', 'Josh Macy')


# Email Sent
Emails_Sent_JoshM = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Josh Macy', ['Sent']].sum()

SentPofCont_JoshM = Emails_Sent_JoshM/Number_Contact_JoshM

# Emails Open
Emails_Opened_JoshM = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Josh Macy', ['Opened']].sum()

OpenedPofSent_JoshM = Emails_Opened_JoshM/Emails_Sent_JoshM[0]

# Numbers of Clicks
Clicks_JoshM = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Josh Macy', ['Clicked']].sum()

ClicksPofOpened_JoshM = Clicks_JoshM/Emails_Opened_JoshM[0]

# NUmber of registrantants

Regis_JoshM = 25

ClicksPofOpened_JoshM = Regis_JoshM/Emails_Opened_JoshM[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Josh Macy'

JoshMData = df_merge_col.loc[selected_sp]

selectedEmailStatus = JoshMData['Clicked'] == True

JoshMClicked = JoshMData.loc[selectedEmailStatus]

JoshMClicked.to_excel('JoshMClicked.xlsx')


# Who Clicked
Who_Clicked_JoshM = JoshMClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_JoshM.to_excel('Who Clicked Josh Macy.xlsx')

"""

#######################
# Selecting the people that opened 

selectedEmailStatus = JoshMData['Opened'] == True

JoshMOpened = JoshMData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Josh = JoshMOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Josh.to_excel('Who Opened Josh Macy.xlsx')
"""


############################################
## Joshua Duncan
############################################

# Count of number of countacts
Number_Contact_JoshD = appcount(
        df_merge_col, 'Territory Owner', 'Joshua Duncan')


# Email Sent
Emails_Sent_JoshD = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Joshua Duncan', ['Sent']].sum()

SentPofCont_JoshD = Emails_Sent_JoshD/Number_Contact_JoshD

# Emails Open
Emails_Opened_JoshD = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Joshua Duncan', ['Opened']].sum()

OpenedPofSent_JoshD = Emails_Opened_JoshD/Emails_Sent_JoshD[0]

# Numbers of Clicks
Clicks_JoshD = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Joshua Duncan', ['Clicked']].sum()

ClicksPofOpened_JoshD = Clicks_JoshD/Emails_Opened_JoshD[0]

# NUmber of registrantants

Regis_JoshD = 30

ClicksPofOpened_JoshD = Regis_JoshD/Emails_Opened_JoshD[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Joshua Duncan'

JoshDData = df_merge_col.loc[selected_sp]

selectedEmailStatus = JoshDData['Clicked'] == True

JoshDClicked = JoshDData.loc[selectedEmailStatus]

JoshDClicked.to_excel('JoshDClicked.xlsx')

# Who Clicked
Who_Clicked_JoshD = JoshDClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_JoshD.to_excel('Who Clicked Josh Duncan.xlsx')

"""

#######################
# Selecting the people that opened 

selectedEmailStatus = JoshDData['Opened'] == True

JoshDOpened = JoshDData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_JoshD = JoshDOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_JoshD.to_excel('Who Opened Josh Duncan.xlsx')
"""


############################################
## Kevin Klick
############################################

# Count of number of countacts
Number_Contact_Kevin = appcount(
        df_merge_col, 'Territory Owner', 'Kevin Klick')


# Email Sent
Emails_Sent_Kevin = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Kevin Klick', ['Sent']].sum()

SentPofCont_Kevin = Emails_Sent_Kevin/Number_Contact_Kevin

# Emails Open
Emails_Opened_Kevin = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Kevin Klick', ['Opened']].sum()

OpenedPofSent_Kevin = Emails_Opened_Kevin/Emails_Sent_Kevin[0]

# Numbers of Clicks
Clicks_Kevin = df_merge_col.loc[df_merge_col[
        'Territory Owner'] == 'Kevin Klick', ['Clicked']].sum()

ClicksPofOpened_Kevin = Clicks_Kevin/Emails_Opened_Kevin[0]

# NUmber of registrantants

Regis_Kevin = 63

ClicksPofOpened_Kevin = Regis_Kevin/Emails_Opened_Kevin[0]


# Selecting the people that clicked 
selected_sp = df_merge_col['Territory Owner'] == 'Kevin Klick'

KevinData = df_merge_col.loc[selected_sp]

selectedEmailStatus = KevinData['Clicked'] == True

KevinClicked = KevinData.loc[selectedEmailStatus]

KevinClicked.to_excel('KevinClicked.xlsx')




# Who Clicked
Who_Clicked_Kevin = KevinClicked['Title'].value_counts()
"""
# Save to Excel
Who_Clicked_Kevin.to_excel('Who Clicked Kevin.xlsx')

"""


#######################
# Selecting the people that opened 

selectedEmailStatus = KevinData['Opened'] == True

KevinOpened = KevinData.loc[selectedEmailStatus]


# Counting the tittles
Who_Opened_Kevin = KevinOpened['Title'].value_counts()
"""
# Save the who clicked in a excel
Who_Opened_Kevin.to_excel('Who Opened Kevin.xlsx')
"""
















