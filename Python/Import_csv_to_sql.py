#Import libraries
import pyodbc 
import pandas as pd
import numpy as np
from datetime import datetime

#%%
#Read file

dt = datetime.now()

tmstamp=dt.strftime("%m_%d_%Y_%H_%M_%S")

source_file_path=r'C:\Users\ASUS-PC\Downloads\CsvFiles\film2.csv'

target_file_path= r'C:\Users\ASUS-PC\Downloads\CsvFiles\film2_python_{timestamp}.csv'.format(timestamp=tmstamp)

#Create DF
df = pd.read_csv(source_file_path,sep=';',encoding='latin-1')
df=df.rename(columns={'*Image':'Image'})
#df = df.fillna(value='')
df = df.replace({np.nan:None})#Replace empty columns with null to insert into SQL
#print(df)

#%%
#Create connection with database
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=(localdb)\MSSqlLocalDb;"
            "Database=rocio;"
            "Trusted_Connection=yes;")

cnxn = pyodbc.connect(cnxn_str) # initialise connection

cursor = cnxn.cursor()

cursor.execute("drop table if exists dbo.Movie_python")
cursor.execute("create table dbo.Movie_python" +
"(Year varchar(max) null,Length varchar(max) null,Title varchar(max) null,Subject varchar(max) null,Actor varchar(max) null,Actress varchar(max) null,Director varchar(max) null,Popularity varchar(max) null,Awards varchar(max) null,Image varchar(max) null)")
cnxn.commit()


# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
    cursor.execute("INSERT INTO dbo.Movie_python(Year,Length,Title,Subject,Actor,Actress,Director,Popularity,Awards,Image) values(?,?,?,?,?,?,?,?,?,?)", row.Year,row.Length,row.Title,row.Subject,row.Actor,row.Actress,row.Director,row.Popularity,row.Awards,row.Image)
cnxn.commit()

cursor.close()

#%%
#Export table to a csv file

query= "select * from dbo.Movie_python"
#def convert_table_to_csv(query,cnxn,target_file_path):
sql_query = pd.read_sql_query(query,cnxn)
new_df = pd.DataFrame(sql_query)
#print(new_df)
df.to_csv (target_file_path, index = False)

#Create a dataframe from my sql table
#data = pd.read_sql("SELECT TOP(10) * FROM dbo.Movie_python", cnxn)

del cnxn  # close the connection
