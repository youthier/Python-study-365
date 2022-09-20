###code来自https://blog.csdn.net/qq_55292642/article/details/120106438
from lib2to3.pytree import convert
import os
import xlwings as xw
import pandas as pd   # 引用相关的库
import datetime

folder = os.getcwd()   # 获取当前目录
files = os.listdir(folder)   # 获取当前目录所有文件夹
today = datetime.date.today()
day = pd.to_datetime(today,format='%Y-%m-%d')
files_xlsx = []
for file in files:
    fname,ext = os.path.splitext(file)
    if ext in [".xlsx"] and fname[: 2] != "~$":
        files_xlsx.append(file)   # 筛选出xlsx文件并过滤xlsx隐藏文件

print("已找到如下Excel文件")
for i in files_xlsx:
    print(i,end="\n")
print("按任意键继续：")
input()

for xlsx in files_xlsx:
    print(f"即将拆分文件：\n{xlsx}\n")
    field_name = input("按什么拆分？")

    app = xw.App(visible=True, add_book=False)
    workbook = app.books.open(xlsx)
    worksheet = workbook.sheets[0]

    sheet_names = [j.name for j in workbook.sheets]
    value = worksheet.range('A1').options(pd.DataFrame ,header = 1,
                                        index = False, expand = 'table').value  # 读取要拆分的工作表中的所有数据
    data = value.groupby(field_name)
    for idx, group in data:
        if idx not in sheet_names:
            # new_worksheet = workbook.sheets.add(idx)
            #创建新的工作薄另存数据
            
            
            new_worksheet = workbook.sheets.add()
            workbook.sheets[idx].range("A:CC").api.NumberFormat = "@"
            # range('A2').api.NumberFormat = "0.0"  # 设置为小数格式
            # range('A3').api.NumberFormat = "yyyy-mm-dd"  # 设置为"-"连接的日期格式
            new_worksheet.range('A1').options(index = False).value = group
        workbook.sheets[idx].range('A1').options(index = False).value = group
    workbook.save(files_xlsx+str(day)+'.xlsx')
    workbook.close()
    app.quit()
    
    print(f"\n{xlsx}||拆分完成.")
print("全部拆分完成")
input("按任意键退出")
