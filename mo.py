class student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.__grades = [grades]

    def get_grades(self):
        return self.__grades
    
    def add_grades(self, *grades):
        if all(grade >= 0 and grade <= 100 for grade in grades):
            self.__grades.extend(grades)
        else:
          raise ValueError("Grades must be between 0 and 100")
    def calculate_average(self):
        if len(self.__grades) == 0:
           return 0      
        else:
          return sum(self.__grades) / len(self.__grades)


    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return ("A")
        elif average >= 80:
            return("B")
        elif average >= 70:
            return("C")
        elif average >= 60:
            return("D")
        elif average >= 0 and average <= 59:
            return("F")
        else:
            return("N/A")
    def display_info(self):
       print("Student name:", self.name)
       print("Student id:", self.id)
       print("Grades:", self.get_grades())
       print("Average grade:", self.calculate_average())
       print("Final letter grade:", self.calculate_grade())

    


class undergraduatestudent(student):
    def __init__(self, name, id, grades, major):
      super().__init__(name, id, grades)
      self.major = major

    def display_info(self):
        super().display_info()
        print("Major:", self.major)

class graduatestudent(student):
    def __init__(self, name, id, grades, program_title):
     super().__init__(name, id, grades)
     self.program_title = program_title

    def display_info(self):
        super().display_info()
        print("Program:", self.program_title)

