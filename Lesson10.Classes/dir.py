class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("Hi, I am", self.name)

print(dir())
print(dir(Employee))