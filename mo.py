class student:
    def __init__(self, name, id, grade):
        self.name = name
        self.id = id
        self.grade = grade

    def show_info(self):
        print("Student name:", self.name)
        print("id:", self.id)
        print("grade:", self.grade)
    

class undergraduatestudent(student):
    def __init__(self, name, id, grade, major):
      super().__init__(name, id, grade)
      self.major = major

    def display_info(self):
     print("Student Name:", self.name)
     print("id:", self.id)
     print("Grades:", self.grade)
     print("Major:", self.major)

class graduatestudent(student):
    def __init__(self, name, id, grade, program_title):
     super().__init__(name, id, grade)
     self.program_title = program_title

    def display_info(self):
      print("Student Name:", self.name)
      print("id:", self.id)
      print("Grades:", self.grade)
      print("Program:", self.program_title)

