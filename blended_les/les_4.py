 
# # bankivsikia rahunok

# class Bancomat:
#     def __init__(self, name, surname, balance) -> None:
#         self.name = name
#         self.surname = surname
#         self.balance = balance
        
#     def get_balance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return True
#         else:
#             return False
    
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return True
#         else:
#             return False
    
# my_account = Bancomat("Sergio", 'Siracenco', 2000)
# my_account.deposit(500)
# print(my_account.get_balance())
# my_account.withdraw(1500)
# print(my_account.get_balance())


# ================================

# =============================

# class StudentSystem:
#     def student_list(self, data_list):
#         self.data_list = data_list
#     def grade(self, mark):
#         sys_grade = {1: 'F', 2: 'FX', 3: 'E',
#                      3.5: 'D', 4: 'C', 4.5: 'B', 5: 'A'}
#         sys_grade1 ={
#         "F": 1,
#         "FX": 2,
#         "E": 3,
#         "D": 3.5,
#         "C": 4,
#         "B": 4.5,
#         "A": 5
#     }
        
#         final_mark = sys_grade.get(mark)
#         if isinstance(mark,(float, int)):
#             return final_mark
#         else:
#             return sys_grade1[mark]
        
#     def avg_mark(self):
#         sum = 0
#         for students in self.data_list:
#             sum += students.grade
#         return sum / len(self.data_list)
    
#     def find_student(self):
#         avg_grade = self.avg_mark()
#         for students in self.data_list:
#             if avg_grade == students.grade:
#                 print(students.name)
# class Students:
#     def __init__(self, name, surname, grade, birthday):
#         self.name = name
#         self.surname = surname
#         self.grade = grade
#         self.birthday = birthday
# st_list = [Students('John', 'Doe', 3.5, '17.12.2013'),
#            Students('Dick', 'Back', 5, '15.10.2011')]

# c = StudentSystem()
# c.student_list(st_list)

# print(c.grade('A'))
# print(c.grade(5))



# =========================================


class Detail:
    def __init__(self, name) -> None:
        self.name = name
    def __get__(self, instance, owner):
        
        return self.name
    def __set__(self, instance, name):
        self.name = name
    def __str__(self) -> str:
        return f"{self.name}"
        
class Motor(Detail):
    def __init__(self, name):
        super().__init__(name)
        
class Wheels(Detail):
    def __init__(self, name):
        super().__init__(name)
        
import traceback
class Auto:
    details = []
        
    def __init__(self, def_name=None) -> None:
        if def_name == None:
            (_,_,_,text)=traceback.extract_stack()[-2]
            def_name = text[:text.find('=')].strip()
        self.defined_name = def_name
        
    def add_detail(self, detail):
        self.details.append(detail)
        
    def __repr__(self) -> str:
        return f"Auto {self.defined_name} ({str(self)})"

    def __str__(self) -> str:
        return ', '.join(map(str, self.details))

motor1_5 = Motor("motor 1.5")
koleso = Wheels("wheels 17")        
tavria = Auto()
tavria.add_detail(motor1_5)
tavria.add_detail(koleso)

print(tavria) # str - method

print(repr(tavria))

print(tavria.details[0])
print(tavria.details[1])

# # class SomeObject():
# #     def __init__(self, def_name):
# #         self.defined_name = def_name
# #         globals()[def_name] = self

# # SomeObject("ThisObject")
# # print(ThisObject.defined_name)