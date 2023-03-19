from models import ListOrganizer

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

if __name__ == '__main__':
    # CONFIGs:
    file_path = 'lists/teste.txt'
    save_path = 'lists/organized_list.txt'

    # CREATE LIST:
    listed_items = txt_to_list(file_path)
    # ORGANIZE LIST:
    list_organizer = ListOrganizer(listed_items)
    # SAVE LIST:
    save_list_as(list_organizer.organized_list, save_path)
