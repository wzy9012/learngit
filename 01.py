'''
定义一个学生类
'''
#定义一个空的类
class Student():
    pass
#定义一个对象
mingyue = Student()

#定义一个类，用来描述Python的学生
class PythonStudent():
    name = None
    age = 18
    course = "Python"


    def doHomework(self):
        print("I am doing honework")

        return None


yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)

yueyue.doHomework()