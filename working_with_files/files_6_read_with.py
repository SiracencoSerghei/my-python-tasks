
def get_recipe(path, search_id):
    with open(path, 'r') as fh:
        for line in fh:
            parts = line.strip().split(',')
            if parts[0] == search_id:
                return {
                    "id": parts[0],
                    "name": parts[1],
                    "ingredients": parts[2:]
                }
    return None 

search_id = "60b90c3b13067a15887e1ae4"
path = "/home/sergio/Desktop/my python tasks/working_with_files/ingredients.txt"
print(get_recipe(path, search_id))
