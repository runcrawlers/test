class Student:
    count = 0  # 类属性：在类里面 类方法外面 self.__class__.属性名

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1

    def show(self):
        print(f'姓名{self.name},分数{self.score}')


s1 = Student('张三', 90)
s2 = Student('李四', 90)
print(s1.__class__.count)
