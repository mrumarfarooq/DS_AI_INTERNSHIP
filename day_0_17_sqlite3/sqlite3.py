import pandas as pd

import sqlite3

conn=sqlite3.connect("C:/DS_AI_Internship/0_day17_sqlite3/Database/sample.db")

df=pd.read_sql_query("SELECT * FROM students",conn)

df

df1=pd.read_sql_query("SELECT name, marks FROM students;",conn)
df1

df2=pd.read_sql_query("SELECT name FROM students WHERE marks >= 90;",conn)
df2

