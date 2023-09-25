
def add_employee_to_file(record, path):
    
    fh = open(path, "a")
    
    fh.write(record + "\n")
    
    fh.close()
    
record = "Draked Mikelsson, 29"
path = "/home/sergio/Desktop/my python tasks/working_with_files/employees.txt"

add_employee_to_file(record, path)