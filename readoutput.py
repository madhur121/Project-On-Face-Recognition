import xlsxwriter
from collections import Counter
names=[]
names.clear()
names=open("outputtxt.txt","r").read().splitlines()
for x in names:
   print(x)

col_counter=Counter(names)
print(col_counter)

for item in col_counter:
    print(item,col_counter[item])

workbook=xlsxwriter.Workbook('out.xlsx')
worksheet=workbook.add_worksheet()
worksheet.write(0,0,'NAME')
worksheet.write(0,1,'ATTENDENCE')
row=1
col=0

for item in col_counter:
    col=0
    worksheet.write(row,col,item)
    col=1
    worksheet.write(row,col,col_counter[item])
    row=row+1

workbook.close()





