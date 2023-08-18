import csv
import glob 
import pandas as pd 
import shutil
import time

original = r"Idea5.csv"

start = time.time()
df = pd.read_csv("Idea5.csv")

df.dtypes

df.loc[:,['SNAME']]=df['SNAME'].str.upper()
df.loc[:,['ADDRESS']] = df['ADDRESS'].str.upper()
df.loc[:,['AGE']] += 1 
df.loc[:,['SALARY']] = df.SALARY + 0.02*(df.SALARY)
df.loc[:,['GENDER']]=df['GENDER'].replace('Female','F')
df.loc[:,['GENDER']]=df['GENDER'].replace('Male','M')
df.loc[:,['CONTACT']] = df['CONTACT'].astype(str).radd("+91 ")


#print(df)
df.to_csv(r"V3t.csv")
end = time.time()
print(f"ETL time for 5crore = {end - start}")
