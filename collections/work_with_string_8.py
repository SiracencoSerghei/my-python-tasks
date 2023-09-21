'''Напишіть функцію formatted_grades, яка приймає на вхід словник оцінювання студентів за предмет наступного вигляду:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
І повертає список відформатованих рядків, щоб під час виведення наступного коду:

for el in formatted_grades(students):
    print(el)
Виходила наступна таблиця:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
перший стовпець — ширина 4 символи, вирівнювання по правому краю
другий стовпець — ширина 10 символів, вирівнювання по лівому краю
третій та четвертий стовпець — ширина 5 символів, вирівнювання по центру
вертикальний символ | не входить у ширину стовпця'''


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

def formatted_grades(students):
    students_list = []
    for i, (name, grade) in enumerate(students.items(), start=1):
        if grade in grades:
            score = grades[grade]
        else:
            score = 0
        
        # {i:>4} - праворуч,4 символи 
        # name:<10 - ліворуч, 10 символів
        # grade:^5 - по центру, мінімум 5 символів 
            
        student = f"{i:>4}|{name:<10}|{grade:^5}|{score:^5}"
        students_list.append(student)
    
    return students_list 

for el in formatted_grades(students):
    print(el)