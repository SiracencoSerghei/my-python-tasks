from random import randint, choice


class Position:
    def __init__(self, value) -> None:
        self.value = value

    def get_salary(self):
        return randint(500, 1500)

    def __str__(self) -> str:
        return self.value


class Employee:
    def __init__(self, name: str, position: str = None) -> None:
        self.name = name
        self.position = Position(position) if position else position

    def get_rate(self) -> int:
        if self.position:
            return self.position.get_salary()
        return 0


names = ("Bill", "Gill", "Mary")

positions = ("Manager", "CEO", "Developer", "QA")

employees = []

for i in range(1000):
    employees.append(Employee(f"{choice(names)}-{i}", choice((choice(positions), None))))

print(len(employees))

rand_emp: Employee = employees[randint(0, 999)]

print(rand_emp.get_rate(), rand_emp.position, rand_emp.name)

print(len(list(filter(lambda x: x.get_rate() != 0, employees))))