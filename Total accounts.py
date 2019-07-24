#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:26:40 2019

@author: arthurmendes
"""

import pandas as pd


# Import Salesforce dataset
SF_all = pd.read_csv('report1563913703461.csv')

SF_all.head()


# Create a function to count the number of accounts on each sales representative

def appcount(df, col, x):
    return (df[col] == x).sum()

# Unique Territory Owners

SF_all['Territory Owner'].unique()

'''
array([nan, 'Andrew Card', 'Brian Duffy', 'Claire Stovall', 'Josh Macy',
       'Joshua Duncan', 'Kevin Klick', 'Matt Parrack'], dtype=object)
    
'''


############################################
## Andrew Card'
############################################

# Count of number of countacts
Number_Contact_Andrew = appcount(
        SF_all, 'Territory Owner','Andrew Card')

print(Number_Contact_Andrew)
############################################
## Brian Duffy
############################################

# Count of number of countacts
Number_Contact_Brian = appcount(
        SF_all, 'Territory Owner','Brian Duffy')

print(Number_Contact_Brian)

############################################
## Claire Stovall
############################################

# Count of number of countacts
Number_Contact_Claire = appcount(
        SF_all, 'Territory Owner','Claire Stovall')

print(Number_Contact_Claire)

############################################
## Josh Macy
############################################

# Count of number of countacts
Number_Contact_JoshM = appcount(
        SF_all, 'Territory Owner','Josh Macy')

print(Number_Contact_JoshM)

############################################
## Joshua Duncan
############################################

# Count of number of countacts
Number_Contact_JoshD = appcount(
        SF_all, 'Territory Owner','Joshua Duncan')

print(Number_Contact_JoshD)

############################################
## Kevin Klick
############################################

# Count of number of countacts
Number_Contact_Kevin = appcount(
        SF_all, 'Territory Owner','Kevin Klick')

print(Number_Contact_Kevin)

############################################
## Matt Parrack
############################################

# Count of number of countacts
Number_Contact_Matt = appcount(
        SF_all, 'Territory Owner','Matt Parrack')

print(Number_Contact_Matt)
