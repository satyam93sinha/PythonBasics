class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update

class Child(Mapping):
    def update(self, diction):
        for keys, values in diction.items():
            self.item_list.append({keys:values})
