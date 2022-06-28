import sqlite3
from xlsxwriter.workbook import Workbook
workbook = Workbook('user_love.xlsx')
worksheet = workbook.add_worksheet()
# 传入数据库路径，db.s3db或者test.sqlite
conn=sqlite3.connect('db.sqlite3')
c=conn.cursor()
mysel=c.execute("select rate, rank from perfumes_perfume")
for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
workbook.close()