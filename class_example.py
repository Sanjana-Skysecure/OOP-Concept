class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = []

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")
    
    def add_grade(self, grade):
        """Add a grade to the student's record"""
        self.grades.append(grade)
        print(f"✅ Grade {grade} added for {self.name}")
    
    def calculate_average(self):
        """Calculate and return the average grade"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def show_grades(self):
        """Display all grades and average"""
        if self.grades:
            print(f"\n📊 Grades for {self.name}:")
            print(f"   Individual grades: {self.grades}")
            print(f"   Average: {self.calculate_average():.2f}")
        else:
            print(f"No grades recorded for {self.name}")

# Execution
if __name__ == "__main__":
    s1 = Student("Sanjana", "Python Backend Development")
    s1.display_info()
    s1.add_grade(85)
    s1.add_grade(92)
    s1.add_grade(88)
    s1.show_grades()
