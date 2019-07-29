#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:02:41 2019

@author: arthurmendes

repository:
/Users/arthurmendes/Desktop/Beckers Analysis
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


# The rest
rest = pd.read_csv('report1563909905865.csv')


# Import HubSpot Dataset
rest_HS = pd.read_csv('events.csv')


# Merge datasets on "Email"
df_merge_rest = pd.merge(rest, rest_HS, on='Email')


# Full Merge

frames = [df_merge_rest, df_merge_col]

full_merge = pd.concat(frames)

# Create a function to count the number of accounts on each sales representative

def appcount(df, col, x):
    return (df[col] == x).sum()

# Unique list of states
States_count = full_merge['Mailing State/Province (text only)'].value_counts()

States_count.to_excel('States Count.xls')


# Alabama
Alabama = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('AL|Alabama',
        case=True, 
        regex=True) == True]
    

# Alaska 
Alaska = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Alaska',
        case=True, 
        regex=True) == True]
# Arizona
    
Arizona = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('AZ|Arizona',
        case=True, regex=True) == True]

    
# Arkansas
    
Arkansas = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('AR|Arkansas',
        case=True, regex=True) == True]
    
# California
    
California = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('California',
        case=True, regex=True) == True]
    
# Colorado
    
Colorado = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('CO|Colorado',
        case=True, regex=True) == True]
    
# Connecticut

Connecticut = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('CT|Connecticut',
        case=True, regex=True) == True]
    
    
# Delaware
Delaware = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Delaware',
        case=True, regex=True) == True]
    
    
# District of Columbia

Columbia = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Columbia',
        case=True, regex=True) == True]
    
# Florida
    
Florida = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Florida|FL',
        case=True, regex=True) == True]
    
# Georgia
    
Georgia = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Georgia|GA',
        case=True, regex=True) == True]
    

# Hawaii
Hawaii = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Hawaii',
        case=True, regex=True) == True]
    
# Idaho
    
Idaho = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Idaho',
        case=True, regex=True) == True]
    
# Illinois
Illinois = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('IL|Illinois',
        case=True, regex=True) == True]
    
# Indiana
Indiana = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('IN|Indiana',
        case=True, regex=True) == True]
    
# Iowa
Iowa = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('IA|Iowa',
        case=True, regex=True) == True]
    
# Kansas
Kansas = full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('KS|Kansas',
        case=True, regex=True) == True]

# Kentucky
Kentucky =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('KY|Kentucky',
        case=True, regex=True) == True]
    
# Louisiana
Louisiana =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('LA|Louisiana',
        case=True, regex=True) == True] 
    
# Maine
Maine =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Maine',
        case=True, regex=True) == True] 
    
   # Maryland
Maryland =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('MD|Maryland',
        case=True, regex=True) == True]  
    
    # Massachusetts
Massachusetts =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Massachusetts|MA',
        case=True, regex=True) == True] 
   
    # Michigan
Michigan =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Michigan|MI',
        case=True, regex=True) == True] 
    
    # Minnesota
Minnesota =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Minnesota|MN',
        case=True, regex=True) == True] 
    
    # Mississippi
Mississippi =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Mississippi|MS',
        case=True, regex=True) == True] 
   
    
    # Missouri
Missouri =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Missouri|MO',
        case=True, regex=True) == True] 
    # Montana
Montana =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Montana',
        case=True, regex=True) == True] 
    # Nebraska
Nebraska =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Nebraska',
        case=True, regex=True) == True] 
    
    # Nevada
Nevada =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Nevada|NV',
        case=True, regex=True) == True] 
    
    # New Hampshire
NewHampshire =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('New Hampshire|NH',
        case=True, regex=True) == True] 
    
    # New Jersey
NewJersey =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('New Jersey|NJ',
        case=True, regex=True) == True] 
    
    # New Mexico
NewMexico =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('New Mexico|NM',
        case=True, regex=True) == True] 
    
    # New York
NewYork =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('New York|NY',
        case=True, regex=True) == True] 
    
    # North Carolina
NorthCarolina =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('North Carolina|NC',
        case=True, regex=True) == True] 
    
    # North Dakota
NorthDakota =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('North Dakota|ND',
        case=True, regex=True) == True] 
    
      # Ohio
Ohio =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Ohio|OH',
        case=True, regex=True) == True] 
      
    # Oklahoma
Oklahoma =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Oklahoma|OK',
        case=True, regex=True) == True] 
    
    # Oregon
Oregon =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Oregon|OR',
        case=True, regex=True) == True] 
    
    # Palermo
Palermo =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Palermo',
        case=True, regex=True) == True] 
    
    # Pennsylvania
Pennsylvania =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Pennsylvania|PA',
        case=True, regex=True) == True] 
    
    # Puerto Rico
PuertoRico =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Puerto Rico|PR',
        case=True, regex=True) == True] 
    
    # Rhode Island
RhodeIsland =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Rhode Island|RI',
        case=True, regex=True) == True] 
    
    # South Carolina
SouthCarolina =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('South Carolina|SC',
        case=True, regex=True) == True] 
    
    # South Dakota
SouthDakota =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('South Dakota|SD',
        case=True, regex=True) == True] 
    
    # Tennessee
Tennessee =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Tennessee|TN',
        case=True, regex=True) == True]  
    
    # Texas
Texas =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Texas|TX',
        case=True, regex=True) == True]
    
    # Utah
Utah =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Utah|UT',
        case=True, regex=True) == True]
    
    # Vermont
Vermont =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Vermont',
        case=True, regex=True) == True]
    
    # Virginia
Virginia =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Virginia|VA',
        case=True, regex=True) == True]
    
     # Washington
Washington =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Washington|WA',
        case=True, regex=True) == True]

    
     # West Virginia
WestVirginia =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('West Virginia|WV',
        case=True, regex=True) == True]

    
     # Wisconsin
Wisconsin =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Wisconsin|WI',
        case=True, regex=True) == True]
    
    # Wyoming
Wyoming =  full_merge.loc[full_merge['Mailing State/Province (text only)'].str.contains('Wyoming|WY',
        case=True, regex=True) == True]

###############################################################################
## Creating a Analysis
###############################################################################



def calculation(df):
    test = pd.DataFrame(df['Mailing State/Province (text only)'].unique())
    sent_emails = df.loc[df['Sent'] == True] 
    opened_emails = df.loc[df['Opened'] == True]
    clicked = df.loc[df['Clicked'] == True]
    
    
    analysis = {'State' : [test.iloc[0,0]],
                'Sent' : [sent_emails['Sent'].shape[0]],
                'Sent/Contact' : [sent_emails['Sent'].shape[0]/df.shape[0]],
                'Opened' : [opened_emails.shape[0]],
                'Open/Sent' : [opened_emails.shape[0]/sent_emails.shape[0]],
                'Clicks' : [clicked.shape[0]],
                'CLicks/Opened' : [clicked.shape[0]/opened_emails.shape[0]]}
    analysis = pd.DataFrame(analysis)
    return(analysis)


Analysis = calculation(Florida)


list_of_states = [Alabama,
                  Alaska,
                  Arizona,
                  Arkansas,
                  California,
                  Columbia,
                  Colorado,
                  Connecticut,
                  Delaware,
                  Florida,
                  Georgia,
                  Hawaii,
                  Idaho,
                  Illinois,
                  Indiana,
                  Iowa,
                  Kansas,
                  Kentucky,
                  Louisiana, 
                  Maine, 
                  Maryland, 
                  Massachusetts, 
                  Michigan, 
                  Minnesota, 
                  Mississippi, 
                  Missouri,
                  Montana, 
                  Nebraska, 
                  Nevada,
                  NewHampshire, 
                  NewJersey,
                  NewMexico, 
                  NewYork,
                  NorthCarolina,
                  NorthDakota, 
                  Ohio,
                  Oklahoma,
                  Oregon,
                  Pennsylvania,
                  RhodeIsland,
                  SouthCarolina,
                  SouthDakota,
                  Tennessee,
                  Texas,
                  Utah,
                  Vermont,
                  Virginia,
                  Washington,
                  WestVirginia,
                  Wisconsin, 
                  Wyoming,
                  Palermo]





full_analysis = pd.DataFrame(columns =  [ 'State', 
                                         'Sent',
                                         'Sent/Contact',
                                         'Opened',
                                         'Open/Sent',
                                         'Clicks',
                                         'CLicks/Opened'])


full_analysis = pd.DataFrame()

for val in list_of_states:
    full_analysis = pd.concat([calculation(val), full_analysis])
        
    
    
full_analysis.to_excel('State Analysis.xls')        

        
