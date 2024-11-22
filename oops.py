class student:
    grade=10
    name="aryan"
    def intro(self):
        print("hi i am a student")
    def det(self):
        print("my name is ",self.name)
        print("i am in grade",self.grade)

ob=student()
ob=student().intro()
ob=student().det()