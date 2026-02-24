from DataRecorder import Recorder
r=Recorder('表格.xlsx')
r.set.head(['课程','姓名','日期','网址'])
vals= [
    ['Python入门教程','李四','2024-02-24','https://example.com/2'],
     ['数据分析','王五','2024-01-17','https://example.com/3']
    ]
r.add_data(vals)
r.record()#提交