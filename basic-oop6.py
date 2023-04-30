class Student():
    def __init__(self,name,age,gender,subject,kinkao):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.kinkao = kinkao

    def sawatdee(self):
        if self.gender == 'male':
            tail = 'Krab'
        else:
            tail = 'Ka'
        print(f'Hello...{self.name}.{tail}')

    def study(self):
        print(f'I am studying {self.subject}.')

    def eat(self):
        print(f'I ate {self.kinkao}')

class specialStudent(Student):
    def __init__(self, name, age, gender, subject, kinkao, parent):
        super().__init__(name,age,gender,subject,kinkao)
        self.parent = parent

    def sawatdee(self, person = 'friend'):
        if person == 'friend':
            print('Hi my friend')
        else:
            print('......')
    def myCompany(self):
        print(f'I have got the company is called {self.parent}')

if __name__ == '__main__':
    student1 = Student('Mummee','14','Female','Science','Shrimpdong')

    sstudent1 = specialStudent('Foeifoei','15','male','Math','Salmondong','Themarspolar')

    print(sstudent1.name)
    #print(student1.gender)
    student1.sawatdee()
    student1.study()
    print('Have you eaten lunch yet?')
    student1.eat()    
    sstudent1.myCompany()