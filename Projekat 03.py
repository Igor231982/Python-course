#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import gspread
import datetime
from datetime import date
#importing libraries


# In[2]:


from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:\\Users\\Igor\\Downloads\\Igor23-4d4742891ec3.json', scope)
gc = gspread.authorize(credentials)
#setting scope and credentials


# In[3]:


wks = gc.open("Projekat3")
wks1 = wks.worksheet("Pacijenti")
wks2 = wks.worksheet("Doktori")
wks3 = wks.worksheet("Dijagnoze")
df = pd.DataFrame(wks1.get_all_values())
df2 = pd.DataFrame(wks2.get_all_values())
df3 = pd.DataFrame(wks3.get_all_values())
#opening sheets
doktori = wks2.col_values(1)
dijagnoze = wks3.col_values(1)
datumi = wks1.col_values(4)
pacijenti = wks1.col_values(1)
#exporting defined columns 


# In[ ]:


status = ""
def displayMenu():
    status = input("Za pregled pacijenta pritisnite p, za izvjestaje pritisnite i. p/i?: ").lower()
    if status == "p":
        mExam()       
    elif status == "i":
        mReport()
    else:
        print ("Treba da unesete p ili i")
        status = input("Za pregled pacijenta pritisnite p, za izvjestaje pritisnite i. p/i?: ").lower()
#display menu settings

def mExam():
    numPatient = input("Koliko pacijenata zelite da unesete: ")
    while not numPatient.isdigit():
        print("Molimo vas da unesete broj!")
        numPatient = input("Koliko pacijenata zelite da unesete: ")
        continue
    for i in range(int(numPatient)):        
        try:
            name = input("Unesite ime pacijenta: ").capitalize()
            while not name.isalpha():
                print("Pogresan unos, ime moze se sastoji samo od slova")
                name = input("Unesite ime pacijenta: ").capitalize()
            else:
                surname = input("Unesite prezime pacijenta: ").capitalize()
                while not surname.isalpha():
                    print("Pogresan unos, prezime moze se sastoji samo od slova")
                    surname = input("Unesite prezime pacijenta: ").capitalize()        
            nameSurname = str(name + " " + surname)            
#name and surname settings

            print("Unesite datum rodjenja pacijenta")
            db = input("Unesite dan rodjenja: ")
            mb = input("Unesite mjesec rodjenja: ")
            yb = input("Unesite godinu rodjenja: ")
            start = datetime.date(int("1900"),int("01"), int("01"))
#margins of valid date

            birth = datetime.date(int(yb), int(mb), int(db))
            while birth > date.today() or birth < start:
#checking if entered date is valid

                print("Pogresan datum")
                db = input("Unesite dan rodjenja: ")
                mb = input("Unesite mjesec rodjenja: ")
                yb = input("Unesite godinu rodjenja: ")
                birth = datetime.date(int(yb), int(mb), int(db))
            else:
                dateBirth = birth.strftime("%d.%m.%Y")
#converting date to string

            yearDays = 365.2425
            yearPatient = int((date.today() - birth).days / yearDays)
            print(f"Pacijent ima ", yearPatient, " godina")
#calculating age of patient

            print("Unesite datum pregleda pacijenta")
            de = input("Unesite dan pregleda: ")
            me = input("Unesite mjesec pregleda: ")
            ye = input("Unesite godinu pregleda: ")
            exam = datetime.date(int(ye), int(me), int(de))
            while exam < date.today() or exam > date.today():
                print("Pogresan datum")
                de = input("Unesite dan pregleda: ")
                me = input("Unesite mjesec pregleda: ")
                ye = input("Unesite godinu pregleda: ")
                exam = datetime.date(int(ye), int(me), int(de))
            else:
                dateExam = exam.strftime("%d.%m.%Y")               
#converting date to string

            print("Unesite vrijeme pocetka pregleda: ")
            heb = input("Unesite sate pregleda: ")
            meb = input("Unesite minute pregleda: ")
            teb = str(heb + meb)
            timeExb = datetime.time(hour=int(teb[0:2]), minute=int(teb[2:4]))
            timeExamB = timeExb.strftime("%H:%M")
#converting time to string

            print("Unesite vrijeme kraja pregleda: ")
            hee = input("Unesite sate pregleda: ")
            mee = input("Unesite minute pregleda: ")
            tee = str(hee + mee)
            timeExE = datetime.time(hour=int(tee[0:2]), minute=int(tee[2:4]))
            timeExamE = timeExE.strftime("%H:%M")
#converting time to string

            timeFinal = str(datetime.timedelta(hours=(timeExE.hour - timeExb.hour), minutes=(timeExE.minute - timeExb.minute)))
            timefinal2 = pd.to_datetime(timeFinal)
            duration = timefinal2.strftime("%H:%M")
#calculating duration of examination 

            print("Unesite ime i prezime doktora")
            nameDr = input("Unesite ime: ").capitalize()
            while not nameDr.isalpha():
                print("Pogresan unos, ime moze se sastoji samo od slova")
                nameDr = input("Unesite ime: ").capitalize()
            else:
                surnameDr = input("Unesite prezime: ").capitalize()
                while not surnameDr.isalpha():
                    print("Pogresan unos, prezime moze se sastoji samo od slova")
                    surnameDr = input("Unesite prezime: ").capitalize()
            dr = str(nameDr + " " + surnameDr)
            while not dr in doktori:
#checking if entered doctor exist
                print("Pogresan unos, uneseni doktor nije u bazi")
                nameDr = input("Unesite ime: ").capitalize()
                while not nameDr.isalpha():
                    print("Pogresan unos, ime moze se sastoji samo od slova")
                    nameDr = input("Unesite ime: ").capitalize()
                else:
                    surnameDr = input("Unesite prezime: ").capitalize()
                    while not surnameDr.isalpha():
                        print("Pogresan unos, prezime moze se sastoji samo od slova")
                        surnameDr = input("Unesite prezime: ").capitalize()
                dr = str(nameDr + " " + surnameDr)

            diagnosis = input("Unesite dijagnozu: ").capitalize()
            while not diagnosis in dijagnoze:
#checking if diagnosis exist
                print("Pogresan unos, unesena dijagnoza nije u bazi")
                diagnosis = input("Unesite dijagnozu: ").capitalize()
            else:
                print("Zavrsen unos")

            row = [nameSurname, dateBirth, yearPatient, dateExam, timeExamB, timeExamE, duration, dr, diagnosis]
            index = 2
            wks1.insert_row(row,index)
            wks1

        except ValueError:
            print("Pogresan unos, pokusajte ponovo")
            mExam()

        
def mReport():
    print("Za pretragu pacijenta po imenu i prezimenu pritisnite 1")
    print("Za pregled svih pacijenata na odredjen datum pritisnite 2")
    print("Za pregled pacijente po dijagnozi pritisnite 3")
    print("Za pretragu pacijenata koje ste imali u zadnji broj 'N' dana pritisnite 4")
    status = input("Unesite 1/2/3/4?").lower()

    if status == "1":        
        name = input("Unesite ime pacijenta: ").capitalize()
        while not name.isalpha():
            print("Pogresan unos, ime moze se sastoji samo od slova")
            name = input("Unesite ime pacijenta: ").capitalize()
        else:
            surname = input("Unesite prezime pacijenta: ").capitalize()
            while not surname.isalpha():
                print("Pogresan unos, prezime moze se sastoji samo od slova")
                surname = input("Unesite prezime pacijenta: ").capitalize()        
            nameSurname = str(name + " " + surname)
            while not nameSurname in pacijenti:
#checking if entered patient exist
                name = input("Unesite ime pacijenta: ").capitalize()
                while not name.isalpha():
                    print("Pogresan unos, ime moze se sastoji samo od slova")
                    name = input("Unesite ime pacijenta: ").capitalize()
                else:
                    surname = input("Unesite prezime pacijenta: ").capitalize()
                    while not surname.isalpha():
                        print("Pogresan unos, prezime moze se sastoji samo od slova")
                        surname = input("Unesite prezime pacijenta: ").capitalize()        
                    nameSurname = str(name + " " + surname)
            else:    
                print(df[ df[0] == nameSurname ])
                  
                              
    elif status == "2":
        print("Unesite datum pregleda pacijenta")
        de = input("Unesite dan pregleda: ")
        me = input("Unesite mjesec pregleda: ")
        ye = input("Unesite godinu pregleda: ")
        exam = datetime.date(int(ye), int(me), int(de))
        dateExam = exam.strftime("%d.%m.%Y")
        while not dateExam in datumi:
#checking if entered date exist
            print("Pogresan datum, uneseni datum nije u bazi")
            print("Unesite datum pregleda pacijenta")
            de = input("Unesite dan pregleda: ")
            me = input("Unesite mjesec pregleda: ")
            ye = input("Unesite godinu pregleda: ")
            exam = datetime.date(int(ye), int(me), int(de))
            dateExam = exam.strftime("%d.%m.%Y")
        else:
            print(df[ df[3] == str(dateExam) ])       
        
    elif status == "3":
        diagnosis = input("Unesite dijagnozu: ").capitalize()
        while not diagnosis in dijagnoze:
#checking if entered diagnosis exist
            print("Pogresan unos, unesena dijagnoza nije u bazi")
            diagnosis = input("Unesite dijagnozu: ").capitalize()
        else:
            print(df[ df[8] == str(diagnosis) ])
            
    elif status == "4":      
        nPatient = input("Unesite broj dana: ")
        nPatient2 = int(nPatient) +1
        while not nPatient.isdigit():
            print("Molimo vas da unesete broj!")
            nPatient = input("Unesite broj dana: ")
            continue
        n_numb = df.sort_values(by=3, ascending=0)
        n_numb2 = n_numb.head(int(nPatient2))
        print(n_numb2)        
    else:
        print("Pogresan unos")
displayMenu()


# In[ ]:





# In[ ]:





# In[ ]:




