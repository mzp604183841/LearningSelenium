 # 重新复习一次关于python函数参数的问题
 # 参考资料：廖雪峰的python教程


"""位置参数"""
# 其实就是我们常说的参数，因为意义不同，传入的顺序也应该符合定义的顺序
# 举例：计算x的n次方
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s



"""默认参数"""
# 给定函数中某些参数以默认值，当调用时，可以不传入有默认值的参数
# 举例：power(5) 就相当于 power2(5, 2)
# 注意：定义默认参数要牢记一点：默认参数必须指向不变对象！
def power2(x, n=2):
    s = 1
    while n > 0 :
        n = n - 1
        s = s * x
    return s



"""可变参数"""
# 就是将数组或者元祖当做一个参数传入函数，类似OC的数组，参数名称前加星号"*"
# 举例：
def clas(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum



"""关键字参数"""
# 函数定义时，加双星号表示关键字函数，函数内部将其处理为字典形式
# **extra表示把oneDict这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是oneDict的一份拷贝，对kw的改动不会影响到函数外的oneDict。
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)

oneDict = {'point' : 98, 'number' : '001'}
person("王老五", 23, **oneDict)



"""命名关键字参数"""
