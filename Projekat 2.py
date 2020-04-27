#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import requests
import gspread
import random
import re
#importing libraries


# In[2]:


from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Igor\\Downloads\\Igor23-4d4742891ec3.json', scope)
#setting scope and credentials


# In[3]:


gc = gspread.authorize(credentials)
#wks = gc.open("Projekat2").sheet1
wks = gc.open("Projekat2")
wks1 = wks.worksheet("userpass")
wks1
#opening sheet


# In[7]:


usr = wks1.col_values(1)
psw = wks1.col_values(2)
# exporting usernames and passwords


# In[8]:


usps = dict(zip(usr, psw))
print(usps)
#creating dicionary of usernames and passwords


# In[12]:


users = {}
status = ""

def displayMenu():
    status = input("Are you registered user? y/n?").lower()
    if status == "y":
        log_in()
    elif status == "n":
        sign_up()
    else:
        print ("You have to enter y/n")
        status = input("Are you registered user? y/n?").lower()
#defining display menu

def sign_up():
    createLogin = input("Create login name: ")
    while not re.match(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" ,createLogin):
        print("You didn't enter email")
        createLogin = input("Create login name: ")
#checking if valid email is entered
    else:
        while createLogin in usr:
            print("Login name already exist!")
            createLogin = input("Create login name: ")
#checking if email already exist
        else:
            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            passlen = 8
            p =  "".join(random.sample(s,passlen))
            row = [createLogin, p]
            index = 2
            sh = wks1.insert_row(row,index)
            print("Your password is: ", p)
            print("Login successful!")
#generating and showing password
        
def log_in():
    login = input("Enter login name: ")
    passw = input("Enter password: ")
    while login not in usps:
        print("Wrong email or password!")
        login = input("Enter login name: ")
        passw = input("Enter password: ")
#checking if email already exist
    while login in usps:
        newdict = usps[login]

        if passw == newdict:
            print("You are logged in!")
            break
            
        while passw != newdict:    
            print("Wrong email or password!")
            login = input("Enter login name: ")
            passw = input("Enter password: ")
        
displayMenu()


# In[ ]:




