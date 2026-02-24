import csv
#写入多行
#列表嵌套列表
data=[
    ['张三',25,'北京'],
    ['李四',30,'上海'],
    ['王五',28,'广州'],
]
#header表头
header=['姓名','年龄','城市']
with open('1.csv','w',encoding='utf-8-sig') as f:
  #第一步创建一个写入对象
     w=csv.writer(f)
  # #第二部写入表头
     w.writerow((header))
  # #第三部写入对行数据
     w.writerows(data)
#列表嵌套字典
data = [
           {'name':'张三', 'age':25,'city':'北京'},
           {'name':'李四','age': 30,'city':'上海'},
           {'name':'王五','age': 28,'city':'广州'},
]
header=['name','age','city']
with open('2.csv','w',encoding='utf-8-sig') as f:
       #第一步 创建写入文件
       w=csv.DictWriter(f,header)
       #第二步 写入表头
       w.writeheader()
       #第三部写入数据
       w.writerows(data)
