import pandas as pd
import json
import sys
import os
from tabula import read_pdf
from datetime import datetime


def camelotTables(filename):
    import camelot
    tables = camelot.read_pdf(filename)
    for i in tables:
        print(type(i))
        i.to_json('tmp.json')
        import_content('tmp.json')


def tabulaTables(filename):
    df = read_pdf(filename,pages="all",guess=True,multiple_tables=True,)
    print(df)

def extractorTables(filename,API):
    from ExtractTable import ExtractTable
    et_sess = ExtractTable(api_key=API)        
    print(et_sess.check_usage())      
    table_data = et_sess.process_file(filepath=filename, output_format="json", pages="all")
    print(table_data)
    with open(filename.replace('.pdf','.json'),'w+') as outf:
        json.dump(table_data,outf)

def plumberTables(filename):
    import pdfplumber
    pdf = pdfplumber.open(filename)
    page = pdf.pages[0] # extract only first page
    tab = page.extract_table()
    print(tab)  


def import_content(filepath):
    import pymongo
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['test'] # Replace mongo db name
    collection_name = 'collection1' # Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    # data = pd.read_csv(file_res)
    # print('data',data)
    dat = open(file_res, 'r').read()
    # print(dat)
    dat = dat.replace('.','|dot|')
    data_json = json.loads(dat)
    print('json',data_json)    
    db_cm.remove()
    db_cm.insert(data_json,check_keys=False)



while True:
    print('Enter the type of table Extraction Tool you would like to use:')
    print('1. Camelot')
    print('2. Tabula-py')
    print('3. ExtractTable [requies API Key with > 0 remaining attempts]')
    print('4. PDF-plumber')
    print('For option 3 get an trial API key with 10 attempts from  https://extracttable.com/signup/trial.html')
    opt = int(input('Enter option [1-3] (0 to exit) :'))
    if opt == 0:
        break
    filename = input('Enter filename : ')
    if opt == 1:
        camelotTables(filename)
    elif opt == 2:
        tabulaTables(filename)
    elif opt == 3:
        API_key = input('Enter API key : ')
        extractorTables(filename,API_key)
    elif opt == 4:
        plumberTables(filename)
    
        




