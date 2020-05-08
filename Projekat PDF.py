#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pdfkit as pdf
import pandas as pd
import gspread
#importing libraries


# In[2]:


from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Igor\\Downloads\\Igor23-4d4742891ec3.json', scope)
#setting scope and credentials


# In[3]:


gc = gspread.authorize(credentials)
wks = gc.open("Projekat3")
wks1 = wks.worksheet("Pacijenti")
df = pd.DataFrame(wks1.get_all_records())


# In[4]:


html = df.to_html()

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ]

}

pdf = pdf.from_string(html, "Projekat3.pdf", options=options)
print(pdf)


# In[ ]:




