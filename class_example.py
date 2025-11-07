class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Course: {self.course}")

# Execution
if __name__ == "__main__":
    s1 = Student("Sanjana", "Python Backend Development")
    s1.display_info()
