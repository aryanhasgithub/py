class library:
    def __init__(self,book_list,username):
        self.booklist=book_list
        self.name="coforge library"
        self.lended={}
        self.username=username

    def  displaybooks(self):
        for book in self.booklist:
            print(book)

    def  lend(self,username,book):
        if book not in self.booklist:
            print("book is not present in library")
        elif book in self.lended:
            print("book is already lended")  
        else:
            print(f"book has been lended to {username}")      
            self.lended[book]=username

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added")
    
    def returnbook(self,book):
        if book in self.lended:
            del self.lended[book]
            print("book return :)")
        else:
            print("book was not borrowed from us")

if __name__ == '__main__':
    books = library(['IKIGAI','Harry Potter','Room on the Roof','blue umbrella',],"coforge")
    username=input("please write your name: ")

    while True:
        print(f"\nHello {username}, welcome to the {books.name} library. Please choose an option:")
        print("1. Display Books\n2. Lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
        userchoice=input("please chose an option: ")   
                
        if userchoice not in ['1','2','3','4','5']:
            print("pleasse choose a valid option")
        if userchoice == '1':
              books.displaybooks()
        if userchoice == '2':
            book = input("enter book name: ")   
            books.lend(username,book)
        if userchoice == '3':
            book = input("enter book name: ")   
            books.addbook(book)
        if userchoice == '4':
            book = input("enter book name: ")   
            books.returnbook(book)    
        if userchoice == '5':
            print("Thank you for using the library. Goodbye!")
            break       
   



        