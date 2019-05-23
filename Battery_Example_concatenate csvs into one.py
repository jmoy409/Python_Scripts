# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:34:31 2016

@author: jmoy001
"""

import os
import glob
import pandas as pd

#need to change file path. Pulls every document in folder
def addField(indir="C:\\Users\\jmoy001\\Documents\\Battery Report\\Data Pull4"):
    #set file path as child directory
    os.chdir(indir)
    #variable fileList has all files in folder
    fileList=glob.glob("*")
    for filename in fileList:
        df=pd.read_csv(filename, sep=',', header=None)
        df['Manufacturer']= ""
        df['Manufacturer']=[filename.rsplit("10.24.16",1)[0]]*df.shape[0]
        df['Manufacturer'][0]= "Manufacturer"
        df.to_csv(filename,index=None,header=None)
        print(filename)

addField()

#change file path for both indir and outfile.
#indir path is the same as before
#outfile is where your final file will appear. Need to name actual csv file that it will generate
def concatenate(indir="C:\\Users\\jmoy001\\Documents\\Battery Report\\Data Pull4", outfile="C:\\Users\\jmoy001\\Documents\\Battery Report\\Output\\rawdatatest2.csv"):
    #cwd to input directory    
    os.chdir(indir)
    #generate a list of CSV files using glob method
    fileList=glob.glob("*.csv")
    dfList=[]
    File_Count=0
    #colnames=["ID","Model Number","Site","Battery Plant","String","Battery","Installation Date","Manufacture Date","Last G","Ref G","TComp %","Last V","Last T"]
    for filename in fileList:
        print(filename)
        if File_Count==0:
            df=pd.read_csv(filename,header=None)
            dfList.append(df)
            File_Count=+1
        else:
            df=pd.read_csv(filename,header=None)
            df=df[1:]
            dfList.append(df)
    concatDf=pd.concat(dfList,axis=0)
    #concatDf.columns=colnames
    concatDf.to_csv(outfile,index=None,header=None)

#run concatenate command    
concatenate()



#Generator Report
# This script is to pull the month and year and add as columns in report

#varaible set to generate 2015 in year column
t='2015'

#def means define, I am defining a function to run
#indir = in directory, pull the following documents from this folder, which I included the file path
def addField(indir="C:\\Users\\jmoy001\\Documents\\Generator Report\\All Test"):
    os.chdir(indir)
    #I imported os earlier, it is an add on module to use additional features
    #chdir means current directory. So essentailly, I am making the the indirectory the current working directory
    fileList=glob.glob("*")
    #glob is another module add on
    # the "*" pulls all documents in the folder
    for filename in fileList:
        # for loop, fileList has all documents from the folder, filename is parsing through the folder one at a time
        df=pd.read_csv(filename, sep=',', header=None)
        #read each file and load it
        df['Month']= ""
        #generate empty column with Month as header
        df['Year']=t
        #generate 2015 as year from defined variable, t
        df['Month']=[filename.rsplit(t + " - Generator Report",1)[0]]*df.shape[0]
        #generate month in the month column name by pulling the filename and removing - Generator Report
        #ex. Jan 2015 - Generator Report --> Jan
        df['Month'][0]= "Month"
        #naming column header as Month
        df['Year'][0]= "Year"
        #naming column header as Year
        #reason being, pandas adds own additional row header, so we need to change it
        df.to_csv(filename,index=None,header=None)
        print(filename)
    
addField()

def concatenate(indir="C:\\Users\\jmoy001\\Documents\\Generator Report\\All Test", outfile="C:\\Users\\jmoy001\\Documents\\Generator Report\\Output\\All Output.csv"):
    #cwd to input directory    
    os.chdir(indir)
    #generate a list of CSV files using glob method
    fileList=glob.glob("*.csv")
    #fileList will contain every csv file in folder
    dfList=[]
    #create empty list
    File_Count=0
    #create running count for for loop. code will run based on criteria
    for filename in fileList:
        print(filename)
        #prints name of file when I run function
        if File_Count==0:
            #runs command when file_count=0
            #basically, this code runs once, so column header will only appear once
            df=pd.read_csv(filename,header=None)
            #open file
            dfList.append(df)
            #append file onto spreadsheet
            File_Count=+1
        else:
            df=pd.read_csv(filename,header=None)
            df=df[1:]
            dfList.append(df) 
            
    concatDf=pd.concat(dfList,axis=0)
    concatDf.drop_duplicates()
    #drops duplicates
    concatDf.to_csv(outfile,index=None,header=None)
    #save to new csv file
    
concatenate()
#run concatenate command

