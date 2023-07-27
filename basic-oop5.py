class Student():
    def __init__(self,name,gender,subject,position) :
        self.name = name
        self.gender = gender
        self.subject = subject
        self.position = position

    def sawatdee(self):
        if self.gender == "male" :
            tail = "krab"
        else:
            tail = "ka"
        print(f"I am {self.name} {tail}.")

    def hello(self):
        if self.position == "student" :
            print("Hi!! My Friend")
        else:
            print("Hi!! Teacher")


class SpecialStudent(Student):
    def __init__(self,name,gender,subject,position,lunch):
        super().__init__(name,gender,subject,position)
        self.lunch = lunch

    def study(self):
        print(f"I wanna to study {self.subject}.")


class Teacher(Student):
    def __init__(self,name,gender,subject,position):
        super().__init__(name,gender,subject,position)

    

if __name__ == "__main__" :
    student1 = Student("Mee","female","Math","student")
    teach = Teacher("Neang","male","Redteam","teacher")
    special = SpecialStudent("Cat","male","Science","student","Currychicken")

    student1.sawatdee()
    special.study()
    special.hello()
    teach.hello()
