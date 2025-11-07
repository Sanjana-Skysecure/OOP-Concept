class FileHandler:
    def write_data(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)
        print(f"✅ Data written to {filename}")

    def read_data(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"📖 Reading from {filename}:\n{content}")

# Execution
if __name__ == "__main__":
    handler = FileHandler()
    handler.write_data("sample.txt", "Learning OOP Concepts in Python!")
    handler.read_data("sample.txt")
