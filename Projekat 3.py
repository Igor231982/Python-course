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


wks = gc.open("Projekat3").sheet1
wks2 = gc.open("Projekat3").get_worksheet(1)
wks3 = gc.open("Projekat3").get_worksheet(2)
df = pd.DataFrame(wks.get_all_values())
df2 = pd.DataFrame(wks2.get_all_values())
df3 = pd.DataFrame(wks3.get_all_values())
#opening sheets
doktori = wks2.col_values(1)
dijagnoze = wks3.col_values(1)
datumi = wks.col_values(4)
pacijenti = wks.col_values(1)
#exporting defined columns 


# In[4]:


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
                print("Pogresan unos")
                name = input("Unesite ime pacijenta: ").capitalize()
            else:
                surname = input("Unesite prezime pacijenta: ").capitalize()
                while not surname.isalpha():
                    print("Pogresan unos")
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
                print("Pogresan unos")
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
                print("Pogresan unos")
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
                print("Pogresan unos")
                nameDr = input("Unesite ime: ").capitalize()
            else:
                surnameDr = input("Unesite prezime: ").capitalize()
                while not surnameDr.isalpha():
                    print("Pogresan unos")
                    surnameDr = input("Unesite prezime: ").capitalize()
            dr = str(nameDr + " " + surnameDr)
            while not dr in doktori:
#checking if entered doctor exist
                print("Pogresan unos")
                nameDr = input("Unesite ime: ").capitalize()
                while not nameDr.isalpha():
                    print("Pogresan unos")
                    nameDr = input("Unesite ime: ").capitalize()
                else:
                    surnameDr = input("Unesite prezime: ").capitalize()
                    while not surnameDr.isalpha():
                        print("Pogresan unos")
                        surnameDr = input("Unesite prezime: ").capitalize()
                dr = str(nameDr + " " + surnameDr)

            diagnosis = input("Unesite dijagnozu: ").capitalize()
            while not diagnosis in dijagnoze:
#checking if diagnosis exist
                print("Pogresan unos")
                diagnosis = input("Unesite dijagnozu: ").capitalize()
            else:
                print("Zavrsen unos")

            row = [nameSurname, dateBirth, yearPatient, dateExam, timeExamB, timeExamE, duration, dr, diagnosis]
            index = 2
            wks.insert_row(row,index)
            wks

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
            print("Pogresan unos")
            name = input("Unesite ime pacijenta: ").capitalize()
        else:
            surname = input("Unesite prezime pacijenta: ").capitalize()
            while not surname.isalpha():
                print("Pogresan unos")
                surname = input("Unesite prezime pacijenta: ").capitalize()        
            nameSurname = str(name + " " + surname)
            while not nameSurname in pacijenti:
                name = input("Unesite ime pacijenta: ").capitalize()
                while not name.isalpha():
                    print("Pogresan unos")
                    name = input("Unesite ime pacijenta: ").capitalize()
                else:
                    surname = input("Unesite prezime pacijenta: ").capitalize()
                    while not surname.isalpha():
                        print("Pogresan unos")
                        surname = input("Unesite prezime pacijenta: ").capitalize()        
                    nameSurname = str(name + " " + surname)
            else:    
                cell = wks.find(nameSurname)
                roww = ("%s" % (cell.row))
                pRow = wks.row_values(roww)
#searching a row in sheet for entered patient
                print(pRow)                    
                              
    elif status == "2":
        print("Unesite datum pregleda pacijenta")
        de = input("Unesite dan pregleda: ")
        me = input("Unesite mjesec pregleda: ")
        ye = input("Unesite godinu pregleda: ")
        exam = datetime.date(int(ye), int(me), int(de))
        dateExam = exam.strftime("%d.%m.%Y")
        while not dateExam in datumi:
            print("Pogresan datum")
            print("Unesite datum pregleda pacijenta")
            de = input("Unesite dan pregleda: ")
            me = input("Unesite mjesec pregleda: ")
            ye = input("Unesite godinu pregleda: ")
            exam = datetime.date(int(ye), int(me), int(de))
            dateExam = exam.strftime("%d.%m.%Y")
        else:
            cell = wks.find(dateExam)
            roww = ("%s" % (cell.row))
            dRow = wks.row_values(roww)
#searching a row in sheet for entered date
            print(dRow)       
    elif status == "3":
        diagnosis = input("Unesite dijagnozu: ").capitalize()
        while not diagnosis in dijagnoze:
            print("Pogresan unos")
            diagnosis = input("Unesite dijagnozu: ").capitalize()
        else:
            cell = wks.find(diagnosis)
            roww = ("%s" % (cell.row))
            dgRow = wks.row_values(roww)
#searching a row in sheet for entered patient
            print(dgRow)
    elif status == "4":      
        nPatient = input("Unesite broj dana: ")
        while not nPatient.isdigit():
            print("Molimo vas da unesete broj!")
            nPatient = input("Unesite broj dana: ")
            continue     
    else:
        print("Pogresan unos")
displayMenu()


# In[ ]:




