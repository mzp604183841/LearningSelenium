

# 读取图片转换成二进制编码
# with open('searchImage.jpg', 'rb') as f:
#     print(f.read())


try:
    with open('searchImage.jpg', 'r', encoding='gbk') as f:
        print(f.read())
except UnicodeError as e:  # 有意思的是，找不准对应的python Error类型，都不能顺利执行
    print("》《》《》《》《》《》《")
    print(e)
finally:
    print("测试哦结束")
