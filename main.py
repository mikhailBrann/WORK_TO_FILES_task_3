import os,pprint

file_name = 'recipes.txt'
os_separator = os.path.sep
path_to_file = 'files' + os_separator
files_list = []

# получаем все файлы из директории files
with os.scandir(path_to_file) as file_list:  
    for file_ in file_list:
        if file_.is_file():
           files_list.append(path_to_file + file_.name)

pprint.pprint(files_list)
