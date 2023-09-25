
def total_salary(path):
    total = 0.0
    
    file = open(path, 'r')
    line = file.readline()
    
    while line:
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[1].replace('.', '', 1).isdigit():
            salary = float(parts[1])
            total += salary
        
        line = file.readline()
        
    file.close()
    
    return total


# file_path = 'salary.txt'
file_path = '/home/sergio/Desktop/my python tasks/working_with_files/salary.txt'

total = total_salary(file_path)
print(f'Загальна сума зарплати: {total}')
