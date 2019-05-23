# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:36:39 2017
Script used to open, modify, and convert TGZ file to a CSV file.
Draft 1
@author: jmoy001
"""

import tarfile
import pandas as pd

#Able to pull file, need to get other 3 paths aside from S6a
lst=[]
t = tarfile.open("tgz_file", "r")
for filename in t.getnames():
    try:
        f = t.extractfile(filename)
        Data = f.readlines()
        print(filename, ':', Data)
        lst.append(Data)
    except:
        print('ERROR: Did not find %s in tar archive' % filename)

final_lst=[]
for i in lst:
    for j in i:
        #make each row of data a list and put quotes around each item
        a=str(j).split(',')
        final_lst.append(a)

time_stamp_lst=[]
location_lst=[]
path_lst=[]
volume_lst=[]

for m in final_lst:
    #separate by column of data
    time_stamp_lst.append(m[0])
    location_lst.append(m[1])
    path_lst.append(m[2])
    volume_lst.append(m[3])

#rename column names
time_stamp_lst[0]="Time_Stamp"
location_lst[0]="Market"
path_lst[0]="Path"
volume_lst[0]="Volume_KB"

#remove characters in columns
time_stamp_lst_final = []
for p in time_stamp_lst:
    a=p.strip("'b")
    time_stamp_lst_final.append(a)

volume_lst_final=[]
for w in volume_lst:
    z=w.strip("\\n'")
    volume_lst_final.append(z)

df= pd.DataFrame({'TimeStamp' : time_stamp_lst_final, 'Location' : location_lst, 'Path' : path_lst, 'Volume' : volume_lst_final})
Order= ['TimeStamp', 'Location', 'Path', 'Volume']
#adjust order
df=df[Order]
#write to csv
df.to_csv('csv_file', header=False,index=False)


