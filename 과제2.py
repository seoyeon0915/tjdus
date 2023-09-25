"""class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"{self.name}: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    c1 = Customer('Lily', 45000)
    c2 = Customer('Bob')
    c3 = Customer('Tom', 30000)
    print(c1, c2, c3)

    c1.deposit(10000)
    c2.deposit(20000)
    c3.withdraw(30000)
    print(c1, c2, c3)

    c2.withdraw(50000)
    print(c1, c2, c3)

    print(c3.withdraw(10000), c2.deposit(10000))
    print(c1, c2, c3)"""

"""class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Pet):
    def bark(self, n):
        for _ in range(3):
            print("bark!")

    def human_age(self):
        return self.age * 4
    
class Cat(Pet):
    def meow(self, n):
        for _ in range(2):
            print("meow~")

    def human_age(self):
        return self.age * 4
    
if __name__ == "__main__":
    popo = Dog('popo', 10)
    popo.bark(3)
    print(popo.name, '의 나이:', popo.age)
    print('사람 나이로 환산:', popo.human_age())

    pipi = Cat('pipi', 5)
    pipi.meow(2)
    print(pipi.name, '의 나이:', pipi.age)
    print('사람 나이로 환산:', pipi.human_age())"""

from abc import ABC, abstractmethod

class Item(ABC):
    count = 0  

    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1

    @abstractmethod
    def getprice(self):
        pass  

class Book(Item):
    
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

    def getprice(self):
        return self.price

    def __str__(self):
        return f"책 제목: {self.title}, 가격: {self.price}원, 페이지 수: {self.pages}, 저자: {self.author}"

class Magazine(Item):
    def __init__(self, title, price, issue_number):
        super().__init__(title, price)
        self.issue_number = issue_number

    def getprice(self):
        return self.price

    def __str__(self):
        return f"잡지 제목: {self.title}, 가격: {self.price}원, 이슈 번호: {self.issue_number}"

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)

    print(book1, '\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
    print('총', Item.count, '권')

    print('소나기의 가격:', book1.getprice(), '원')
    print('메밀꽃 필 무렵의 가격:', book2.getprice(), '원')
    print('보그의 가격:', magazine1.getprice(), '원')