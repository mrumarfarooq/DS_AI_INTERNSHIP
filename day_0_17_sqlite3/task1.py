#task 1
import pandas as pd

import sqlite3

conn=sqlite3.connect(r"C:\DS_AI_Internship\0_day17_sqlite3\Database\internship.db")

df=pd.read_sql_query("SELECT name, track FROM interns",conn)

df
