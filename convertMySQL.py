import sqlite3 as sql
import pandas as pd
import os

clear = lambda : os.system("cls")

print("1.")
print("Перед работой введите название .db файла")
print("Before you work, enter the name of the .db file")
DBNAME = input()

conn = sql.connect(DBNAME)
curs = conn.cursor()

clear()

print("2.")
print("Выберите формат для конвертирования: .xlsx, .csv, .html")
print("Select format for conversion: .xlsx, .csv, .html")
formatToConvert = input()

clear()

print("3.")
print("Напишите название таблицы для экспорта")
print("Write the name of the table to be exported")
tableToExport = input("")

data = pd.read_sql(f"SELECT * FROM {tableToExport}", conn)

clear()

print("4.")
print("Напишите название файла для экспорта")
print("Write the name of the file to be exported")

filename = input()

clear()

if formatToConvert.lower() == ".xlsx":
    data.to_excel(f"{filename}{formatToConvert.lower()}", index=False)
elif formatToConvert.lower() == ".csv":
    data.to_csv(f"{filename}{formatToConvert.lower()}", index=False)
elif formatToConvert.lower() == ".html":
    data.to_html(f"{filename}{formatToConvert.lower()}", index=False)
else:
    print("Формат файла для конвертации неправильный! Проверьте правильность его написания")
    print("The file format for conversion is incorrect! Check if it is spelled correctly")