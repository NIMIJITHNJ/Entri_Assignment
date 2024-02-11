class Teacher():
    def __init__ (self, name, subject,level):
        self.name = name
        self.subject = subject
        self.level = level

    def teach(self):
        return f"Sri/Smt. {self.name} is teaching {self.subject} in {self.level} level"
    
name1 = input('Please enter the teachers name:')
subject1 = input('Enter the subject:')
level1 = input('Enter the level of teaching (eg:-LP/UP/HS/HSS) :')

Teacher1 = Teacher(name1,subject1,level1)

print(Teacher1.teach())