'''装饰器，在代码运行期间给函数动态增加功能的方式'''


#  @property
#  把方法装饰成一个属性来用既有对该属性的校验或者方法，也能直接方便到调用

class Student():
    def __init__(self, name, stu_id):
        self.name = name
        self.stu_id = stu_id

    @property
    def score(self):
        return self.score()

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer')
        if value < 0 or value > 100:
            raise ValueError('score must be in 0-100')
        self.score = value


