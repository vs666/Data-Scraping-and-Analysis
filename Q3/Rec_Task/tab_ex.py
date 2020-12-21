from ExtractTable import ExtractTable
import pymongo
import pandas as pd
import json
import sys
import os

et_sess = ExtractTable(api_key='GP7jC2lARU2TMM7XnlDlwfNCrKB1sXJ7O5gFaeNc')        
print(et_sess.check_usage())      



# table_data = et_sess.process_file(filepath=, output_format="csv")
# To process PDF, make use of pages ("1", "1,3-4", "all") params in the read_pdf function
print(sys.argv)
table_data = et_sess.process_file(filepath=sys.argv[1], output_format="csv", pages="all")



def import_content(filepath):
    # mng_client = pymongo.MongoClient('localhost', 27017)
    # mng_db = mng_client['test'] # Replace mongo db name
    # collection_name = 'collection1' # Replace mongo db collection name
    # db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)
    data = pd.read_csv(file_res)
    print('data',data)
    data_json = json.loads(data.to_json(orient='records'))
    print('json',data_json)
    
    # db_cm.remove()
    # db_cm.insert(data_json,check_keys=False)


for i in table_data:
    print(i)
    import_content(i)