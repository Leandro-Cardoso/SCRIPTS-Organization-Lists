from models import ListOrganizer

import json

def txt_to_list(file_path) -> list:
    '''Create list using file .txt'''
    with open(file_path, 'r', encoding = 'utf-8') as file:
        lines = file.readlines()
        file.close()
    for n in range(len(lines)):
        lines[n] = lines[n][:-1]
    return lines

def save_list_as(listed_items, save_path = 'organized_list.txt'):
    '''Save listed items as reported file type'''
    with open(save_path, 'w') as file:
        for item in listed_items:
            file.write(str(item) + '\n')
        file.close()

# LOAD CONFIGs:
config_file_path = './lists_organizer/config.json'
with open(config_file_path) as config_file:
    configs = json.load(config_file)
    config_file.close()

# CREATE LIST:
file_path = configs['file_path']
listed_items = txt_to_list(file_path)

# ORGANIZE LIST:
is_sorted_list = configs['is_sorted_list']
is_reverse = configs['is_reverse']
is_non_duplicate_list = configs['is_non_duplicate_list']
list_organizer = ListOrganizer(listed_items = listed_items, is_sorted_list = is_sorted_list, is_reverse = is_reverse, is_non_duplicate_list = is_non_duplicate_list)
organized_list = list_organizer.organized_list

# SAVE LIST:
save_path = configs['save_path']
save_list_as(listed_items = organized_list, save_path = save_path)
