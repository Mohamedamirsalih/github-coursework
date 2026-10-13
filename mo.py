class student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def show_info(self):
        print("Student name:", self.name)
        print("id:", self.id)
        print("grade:", self.grade)
    

student1 = student("Mohamed", 2501306, 89)
student1.show_info()