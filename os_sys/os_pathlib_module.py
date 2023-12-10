import os
import pathlib
def is_folder_in_catalog(searching_folder, catalog):
    if searching_folder in catalog:
        print('Current working directory has directory "test_folder".')
    else:
        print('Current working directory DON\'T has directory "test_folder".')

active_catalog =  os.environ['HOME']
print('Домашній каталог активного користувача(Environ): ', active_catalog)

pgid = os.getpgid(0)
print("Ідентифікатор групи процесів (Process group ID):", pgid)
print('CPU Count (number of processors): ', os.cpu_count())
current_directory = os.getcwd()
print("Current directory: ", current_directory)
# result = os.popen('ls').read()
result = os.listdir(current_directory)
is_folder_in_catalog('test_folder', result)
create_new_folder = os.system("mkdir test_folder") # return status for creating 'test_folder' => 0 == success...
print("return status for creating 'test_folder' => (0 == success...)  status == ", create_new_folder)
current_directory = (os.getcwd())
result = os.listdir(current_directory)
is_folder_in_catalog('test_folder', result)

# ================================

# absolute path...

print('with OS: ', os.path.abspath('.'))
print('with pathlib: ', pathlib.Path('.').absolute())

# methods to work with file:

# Get the full path to the current script or module
script_path = __file__
print('script path: ', script_path)
# Create a Path object using the script path
script_path_object = pathlib.Path(script_path)
print('script_path_object: ', script_path_object)
# Resolve the path to obtain the absolute path
resolved_script_path = script_path_object.resolve()
print('Resolved: ', resolved_script_path)
# Get the parent directory of the script
script_directory = resolved_script_path.parent
print('scrip_directoru: ', script_directory)
# Specify the file path relative to the script directory
file_path = script_directory / 'test_text.txt'
# Create and write to the file
with open(file_path, 'w') as file:
    file.write('Hello, this is a test file.')

file_methods = [m for m in dir(file_path) if not m.startswith('_')]
# print(file_methods)

# delete file:

# os.remove(file_path)


# ==================================

print(pathlib.Path.cwd())

# create path

print(pathlib.Path('usr').joinpath('local').joinpath('bin'))
print(pathlib.Path('usr') / 'local' / 'bin')

# ======================================
# list current directory
current_iterdir = pathlib.Path('.').iterdir() # generator of directory list
print(current_iterdir)
for f in current_iterdir:
    print(f)
    
# ======================================




