class Student():
    name = None
    nickname = None
    age = None
    grade = None
    subject = None

    def __init__(self,name,nickname,age,grade,gender,subject):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.grade = grade
        self.gender = gender
        self.subject = subject
    
    def study(self):
        print(f'I would love to study {self.subject}')

    def hello(self):
        if self.gender == 'male' :
            tail = 'Krab'
            callme = 'im'
        else :
            tail = 'ka'
            cellme = 'eieiei'
        print(f'Hello!!! {self.name} {tail}')
        
        
class SpecialStudent(Student):
    def __init__(self, name, age, grade,gender, subject, parent):
        super().__init__(name,age,grade,gender, subject,parent)
        self.parent = parent    

    def sawatdee(self):
        print(f'I am {self.name}.')

    def myMom(self):
        print(f'My name mother is..{self.parent}')

class Teacher(Student):

    def __init__(self,name,age,subject):
        self.name = name
        self.age = age
        self.subject = subject

    def teach(self):
        print(f'{self.name} is teaching {self.subject}')

if __name__ =='__main__':
    student1 = Student('Nana','nan','19','grade12','female','math')
    student2 = Student('Manow','now','12','grade11','female', 'science')

    teacher1 = Teacher('Master Mee','28','Math')

    special1 = SpecialStudent('oop','16','9','boy','Math','Lyuda')

    print(student1.name)
    student1.study()

    print(f'I am {student2.name}')
    student2.study()

    print(f'Hi..I am {teacher1.name}, Today I will teach {teacher1.subject}')

    print(f'I just see,Is that your mom? What is your mom name?')
    special1.myMom()

    print(f'I am {student1.name}')
    student1.hello

    student2.hello()
