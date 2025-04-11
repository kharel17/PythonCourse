from abc import ABC, abstractmethod

# abstract base class
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.__title = title
        self.__item_id = item_id

    def get_title(self):
        return self.__title

    def get_item_id(self):
        return self.__item_id

    def set_title(self, title):
        self.__title = title

    def set_item_id(self, item_id):
        self.__item_id = item_id

    @abstractmethod
    def display_details(self):
        pass

# Book class
class Book(LibraryItem):
    def __init__(self, title, item_id, author, isbn, year):
        super().__init__(title, item_id)
        self.author = author
        self.isbn = isbn
        self.year = year

    def display_details(self):
        print("Book:", self.get_title(), self.get_item_id(), self.author, self.isbn, self.year)

# Magazine class
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, publisher):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_details(self):
        print("Magazine:", self.get_title(), self.get_item_id(), self.issue_number, self.publisher)

# Library Member
class LibraryMember:
    def __init__(self, member_id, name):
        self.__member_id = member_id
        self.__name = name
        self.__borrowed_items = []

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_borrowed_items(self):
        return self.__borrowed_items

    def borrow_item(self, item):
        self.__borrowed_items.append(item)

    def return_item(self, item):
        if item in self.__borrowed_items:
            self.__borrowed_items.remove(item)

# Library class
class Library:
    def __init__(self):
        self.items = {}
        self.members = {}

    def add_item(self, item):
        self.items[item.get_item_id()] = item

    def register_member(self, member):
        self.members[member.get_member_id()] = member

    def borrow_item(self, member_id, item_id):
        if member_id in self.members and item_id in self.items:
            member = self.members[member_id]
            item = self.items[item_id]
            member.borrow_item(item)
            print(f"{member.get_name()} borrowed {item.get_title()}")

    def return_item(self, member_id, item_id):
        if member_id in self.members and item_id in self.items:
            member = self.members[member_id]
            item = self.items[item_id]
            member.return_item(item)
            print(f"{member.get_name()} returned {item.get_title()}")

# example
lib = Library()

b1 = Book("Python Book", 1, "Anush", "123-456", 2022)
m1 = Magazine("Tech Monthly", 2, "Issue 9", "TechMedia")

lib.add_item(b1)
lib.add_item(m1)

mem1 = LibraryMember(100, "Golu")
lib.register_member(mem1)

lib.borrow_item(100, 1)
lib.borrow_item(100, 2)

b1.display_details()
m1.display_details()
