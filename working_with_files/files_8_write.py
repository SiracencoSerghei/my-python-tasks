

def save_applicant_data(source, output):
    # =============================
    # variant with write():
    
    with open(output, "w") as fh:
        for student in source:
            data_line = f'{student["name"]},{student["specialty"]},{student["math"]},{student["lang"]},{student["eng"]}\n'
            fh.write(data_line)
    
    # =================================
    # variant with writelines():
    
    # data_lines = []
    
    # for student in source:
    #     data_line = f'{student["name"]},{student["specialty"]},{student["math"]},{student["lang"]},{student["eng"]}\n'
    #     data_lines.append(data_line)
        
    # with open(output, "w") as fh:
    #     fh.writelines(data_lines)
        
    
# Example of using the function:
applicant_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output_file = "/home/sergio/Desktop/my python tasks/working_with_files/applicant_data.txt"
save_applicant_data(applicant_list, output_file)