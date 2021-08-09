class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'姓名:{self.name},年龄:{self.age}')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def show(self):
        super().show()  # SchoolMember.show(self)
        print(f'工资是{self.salary}')


class Student(SchoolMember):
    def __init__(self, name, age, score):
        SchoolMember.__init__(self, name, age)
        self.score = score

    def show(self):
        super().show()
        print(f'分数是{self.score}')


teacher1 = Teacher('韩梅梅', 25, 6000)
teacher1.show()
student1 = Student('李强', 17, 99)
student1.show()
