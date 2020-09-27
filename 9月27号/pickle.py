# 序列化，即将内存中的数据转换成可存储或者可传输的过程

import pickle
import json

# d = dict(name='Edward', age=28, hight=180)
# d_str = pickle.dumps(d)
# print(d_str)
# 以上的方法只能用于python语言自己，不够通用
# 最好的方法是转换成标准格式的字符串，例如 XML JSON

# JSON
j = dict(band='五条人', hotSong='pigs in the city')
j_str = json.dumps(j)
print(j_str)

jj = json.loads(j_str)
print(jj)


class Student(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


def student2dict(stu):
    return {
        'name': stu.name,
        'age': stu.age,
        'height': stu.height
    }


bob = Student('Bob', 25, 180)
bob_str = json.dumps(bob, default=student2dict)
print(bob_str)