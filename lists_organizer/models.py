class ListOrganizer():
    '''Organize a list'''
    def __init__(self, listed_items = [], is_sorted_list = True, is_reverse = False,is_non_duplicate_list = True):
        self.listed_items = listed_items
        self.is_sorted_list = is_sorted_list
        self.is_reverse = is_reverse
        self.is_non_duplicate_list = is_non_duplicate_list
        self.organized_list = self.listed_items

        if is_sorted_list:
            self.organized_list = sorted(self.organized_list, reverse = self.is_reverse)
            
        if is_non_duplicate_list:
            self.organized_list = self.remove_duplicates(self.organized_list)

    def remove_duplicates(self, listed_items) -> list:
        '''Remove duplicate in list'''
        listed_items[:] = [n for i, n in enumerate(listed_items) if i == listed_items.index(n)]
        return listed_items
