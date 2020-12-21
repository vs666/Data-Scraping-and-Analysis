import camelot
from datetime import datetime

c1 = 0

while True:

    filename = input('Enter filename : ')
    tables = camelot.read_pdf(filename)
    c2 = 0
    print(tables)
    for i in tables:
        print('a',i)
        # i.to_csv(str(c1)+'_'+str(c2)+'_'+datetime.today().strftime('%Y_%m_%d_%H_%M_%S')+'_table.csv')
        c2 += 1
    c1 += 1
