class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
        

   
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    
    def books(self):
        return [contract.book for contract in self.contracts()]

   
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    
    def total_royalties(self):
        return (sum(contract.royalties for contract in self.contracts()))

    pass




class Book:

    all = []

    def __init__(self, title):
        self.title = title 
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    pass

    def authors(self):
        return [contract.author for contract in self.contracts()]





class Contract:

    all =[]

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author 
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Invalid author type")
        self._author = value

    @property
    def book(self):
        return self._book 
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Invalid book type")
        self._book = value

    @property
    def date(self):
        return self._date 

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Invalid date type")
        self._date = value

    @property
    def royalties(self):
        return self._royalties 

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception ("Value must be an int between 0 and 100")
        self._royalties = value 

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


    pass