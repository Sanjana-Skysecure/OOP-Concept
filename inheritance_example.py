class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_details(self):
        print(f"Name: {self.name}, Role: {self.role}")

class Manager(Employee):
    def __init__(self, name, role, team_size):
        super().__init__(name, role)
        self.team_size = team_size

    def show_details(self):
        super().show_details()
        print(f"Team Size: {self.team_size}")

# Execution
if __name__ == "__main__":
    m1 = Manager("Sanjana", "Project Manager", 5)
    m1.show_details()
