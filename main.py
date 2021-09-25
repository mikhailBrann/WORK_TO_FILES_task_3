import os

def sorted_files(result_file_name, dir_name):
    os_separator = os.path.sep
    path_to_file = dir_name + os_separator
    files_list = []

    # получаем все файлы из директории files и записываем в список
    with os.scandir(path_to_file) as file_list:  
        for file_ in file_list:
            if file_.is_file():
                with open(path_to_file + file_.name, 'r', encoding="utf-8") as open_file:
                    text_in_file = open_file.readlines()
                    files_list.append({'file_name': file_.name, 'readlines_count': len(text_in_file), 'text': text_in_file})

    # сортируме список
    files_list = sorted(files_list, key=lambda file_: file_['readlines_count'])

    # записываем все в результирующий файл
    with open(result_file_name, 'a', encoding="utf-8") as result_file:
        for file_ in files_list:
            result_file.write(f"{file_['file_name']}\n")
            result_file.write(f"{file_['readlines_count']}\n")
            for text in file_['text']:
                result_file.write(f"{text.strip()}\n")


sorted_files('result.txt', 'files')