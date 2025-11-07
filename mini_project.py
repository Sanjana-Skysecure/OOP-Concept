class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role

    def get_details(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Role: {self.role}"


class Manager(Employee):
    def __init__(self, emp_id, name, role, team_size):
        super().__init__(emp_id, name, role)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"


class EmployeeFileHandler:
    def save_to_file(self, filename, employees):
        with open(filename, 'w') as file:
            for emp in employees:
                file.write(emp.get_details() + "\n")
        print(f"✅ Saved {len(employees)} employees to {filename}")

    def read_from_file(self, filename):
        print(f"\n📂 Reading Employee Records from {filename}:")
        with open(filename, 'r') as file:
            print(file.read())


if __name__ == "__main__":
    e1 = Employee(1, "Sanjana", "Backend Developer")
    e2 = Manager(2, "Ruchitha", "Project Manager", 4)

    handler = EmployeeFileHandler()
    handler.save_to_file("employees.txt", [e1, e2])
    handler.read_from_file("employees.txt")
