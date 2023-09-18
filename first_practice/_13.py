from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    
    for i in Path(path).iterdir():
        if i.is_dir():
            folders.append(i.name)
        if i.is_file():
            files.append(i.name)
            
    return files, folders

print(parse_folder('/home/sergio/Desktop/my python tasks'))

