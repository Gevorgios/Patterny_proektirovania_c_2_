# from abc import ABC, abstractmethod
#
# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
# class LightOnCommand(Command):
#     def execute(self):
#         print("Light is on")
#
# class LightOffCommand(Command):
#     def execute(self):
#         print("Light is off")
#
# class RemoteControl():
#     def __init__(self):
#         self.command = None
#
#     def set_command(self, command):
#         self.command = command
#
#     def press_button(self):
#         self.command.execute()
#
# light_on = LightOnCommand()
# light_off = LightOffCommand()
#
# remote_control = RemoteControl()
#
# remote_control.set_command(light_on)
# remote_control.press_button()
#
# remote_control.set_command(light_off)
# remote_control.press_button()



# 2


# from abc import ABC, abstractmethod
#
#
#
# class NumberSet(ABC):
#     @abstractmethod
#     def get_numbers(self):
#         pass
#
#
#
# class FileNumberSet(NumberSet):
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self._create_numbers_file()
#
#     def _create_numbers_file(self):
#         with open(self.file_path, 'w') as file:
#             file.write("10 20 30 40 50")
#
#     def get_numbers(self):
#         with open(self.file_path, 'r') as file:
#             numbers = [int(num) for num in file.read().split()]
#         return numbers
#
#
#
# class NumberSetProxy(NumberSet):
#     def __init__(self, real_subject, logger):
#         self.real_subject = real_subject
#         self.logger = logger
#
#     def get_numbers(self):
#         numbers = self.real_subject.get_numbers()
#         self.logger.log(f"Accessed number set: {numbers}")
#         return numbers
#
#
#
# class Logger:
#     def log(self, message):
#         with open('log.txt', 'a') as file:
#             file.write(message + '\n')
#
#
#
# file_number_set = FileNumberSet('numbers.txt')
# number_set_proxy = NumberSetProxy(file_number_set, Logger())
#
#
# numbers = number_set_proxy.get_numbers()
# print(numbers)


# 3



# from abc import ABC, abstractmethod
# import pickle
#
# # Singleton Pattern
# class Library:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls.__instance = super().__new__(cls)
#             cls.__instance.books = []
#             cls.__instance.subscribers = []
#         return cls.__instance
#
#     def add_book(self, book):
#         self.books.append(book)
#         self.notify_subscribers(f"Added book: {book.title}")
#
#     def remove_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             self.notify_subscribers(f"Removed book: {book.title}")
#
#     def subscribe(self, subscriber):
#         self.subscribers.append(subscriber)
#
#     def unsubscribe(self, subscriber):
#         self.subscribers.remove(subscriber)
#
#     def notify_subscribers(self, message):
#         for subscriber in self.subscribers:
#             subscriber.update(message)
#
# class Subscriber(ABC):
#     @abstractmethod
#     def update(self, message):
#         pass
#
# class Logger(Subscriber):
#     def update(self, message):
#         with open('log.txt', 'a') as file:
#             file.write(message + '\n')
#
# class SearchStrategy(ABC):
#     @abstractmethod
#     def search(self, keyword):
#         pass
#
# class TitleSearchStrategy(SearchStrategy):
#     def search(self, keyword, books):
#         results = [book for book in books if keyword.lower() in book.title.lower()]
#         return results
#
# class EntityFactory(ABC):
#     @abstractmethod
#     def create_entity(self):
#         pass
#
# class BookFactory(EntityFactory):
#     def create_entity(self, title, author, isbn):
#         return Book(title, author, isbn)
#
# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#
# library = Library()
# logger = Logger()
# library.subscribe(logger)
#
# book_factory = BookFactory()
#
# book1 = book_factory.create_entity("Python Programming", "John Doe","9548548548485")
# book2 = book_factory.create_entity("Design Petterns", "Jane Smith", "344343343434")
#
# library.add_book(book1)
# library.add_book(book2)
#
# with open("library.pkl", 'wb') as file:
#     pickle.dump(library, file)
#
# with open("library.pkl", 'rb') as file:
#     loaded_library = pickle.load(file)
#
# search_strategy = TitleSearchStrategy()
# results = search_strategy.search("Python", loaded_library.books)
# for result in results:
#     print(result.title, result.author, result.isbn)
#
