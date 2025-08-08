#Library Management System
#Features:
#Admin can add/remove books
#Users can borrow/return books
#Track issued books
#Save data in a file
#                           [book class]
#just store book info
class book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_issued=False
    
    def display_book_info(self):
        print(f"{self.book_id} - {self.title} by {self.author} - {'Issued' if self.is_issued else 'Available'}")
    
    def __str__(self):
        return f"[ID: {self.book_id}] '{self.title}' by {self.author}"

#                               [user class]

# Store user information and list of borrowed books.
class User:
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.borrowed_books=[]
    
    def display_info(self):
        print(f"User: {self.user_id} - {self.name}")
        print("Borrowed Books IDs:", self.borrowed_books)

#                           [library class]

# Create a simple Library that stores books and allows Admin to add/remove books.
class Library:
    def __init__(self):
        self.books=[]
        self.users=[]
    
    # --------------------admin functions------------------------------
    
    def add_books(self,book):
        self.books.append(book)
        print(f"Book:- {book.title} Is Added.")
    
    def remove_books(self,book__id):
        for book in self.books:
            if book.book_id==book__id:
                self.books.remove(book)
                print(f"{book.title}  Is Removed Sucessfuly.")
                return
        print("Book Not Found.")

    def show_books(self):
        if not self.books:
            print("No books in library.")
        for book in self.books:
            book.display_info()

    def add_user(self,user):
        self.users.append(user)
        print(f"USER:- {user.name} IS ADDED.")

    # ------------------user functions-----------------------------------
    
    def issue_book(self, book_id,user):
        for book in self.books:
            if book.book_id == book_id and not book.is_issued:
                book.is_issued = True
                user.borrowed_books.append(book_id)
                print(f"Book '{book.title}' issued to {user.name}")
                return
        print("Book not available or already issued.")
    
    def return_book(self,book_id,user):
        for book in self.books:
            if book.book_id==book_id and book.is_issued:
                book.is_issued=False
                if book_id in user.borrowed_books:
                   user.borrowed_books.remove(book_id)
                print(f"Book {book.title} Is Returned By {user.name}.")
                return
        print("Book Was Not Found Or Not Issued")
    
    #----------------tracking function--------------------------------- 

    def show_all_books(self):
        if not self.books:
            print("📂 No books in the library.")
        for book in self.books:
            print(book)
    
    def show_issued_books(self):
        has_issued = False
        print("📚 List of Issued Books:")
        for book in self.books:
            if book.is_issued:
                print(f"- [ID: {book.book_id}] '{book.title}' by {book.author}")
                has_issued = True
        if not has_issued:
            print(" No books are currently issued.")
    
    def find_user_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def show_all_users(self):
        if not self.users:
            print("NO USER FOUND")
            return
        print(" List of All Users:")
        for user in self.users:
             print(f"- [ID: {user.user_id}] {user.name} | Borrowed Books: {user.borrowed_books}")
    
    # -----------------------ALL DATA---------------------------------------
    
    def save_data(self):
        with open("books.txt", "w") as f:
            for book in self.books:
                f.write(f"{book.book_id},{book.title},{book.author},{book.is_issued}\n")
        with open("users.txt", "w") as f:
            for user in self.users:
                f.write(f"{user.user_id},{user.name},{';'.join(map(str, user.borrowed_books))}\n")
        print(" Data saved.")
    
    def load_data(self):
        try:
            with open("books.txt", "r") as f:
                for line in f:
                    book_id, title, author, is_issued = line.strip().split(",")
                    b = book(int(book_id), title, author)
                    b.is_issued = is_issued == "True"
                    self.books.append(b)
        except FileNotFoundError:
            pass

        try:
            with open("users.txt", "r") as f:
                for line in f:
                    user_id, name, borrowed = line.strip().split(",", 2)
                    u = User(int(user_id), name)
                    if borrowed:
                        u.borrowed_books = list(map(int, borrowed.split(";")))
                    self.users.append(u)
        except FileNotFoundError:
            pass

#                           [main function]
def main():
    lib=Library()
    lib.load_data()
    while True:
        print("\n--- Library System ---")
        print("1.ADMIN")
        print("2.LIBRARIAN")
        print("3.USER")
        print("4.EXIT")
        choice = int(input("Enter your choice(1-4):- "))
        match choice:
            # --------------------------ADMIN SECTION------------------------------
            case 1:
                apassword="admin11"
                a_user_password=str(input("WRITE THE PASSWORD:- "))
                if a_user_password ==apassword:
                    print("1. Admin - Add Book")
                    print("2. Admin - Remove Book")
                    print("3. Admin - Register New User")
                    achoice=int(input("WHICH SERVICE YOU WANT(1-3):- "))
                    match achoice:
                        case 1:
                            id=int(input("ENTER ID:- "))
                            title=input("WRITE THE TITLE:- ")
                            author=input("WRITE THE AUTHOR:-")
                            book1=book(id,title,author)
                            lib.add_books(book1)
                        
                        case 2:
                            id=int(input("WRITE ID:- "))
                            lib.remove_books(id)
                        
                        case 3:
                            user_id=int(input("WRITE THE USER ID:- "))
                            name=input("WRITE THE NAME:-")
                            user1=User(user_id,name)
                            lib.add_user(user1)
                        case _:
                            print("INVALID CHOICE")
                else:
                    print("WRONG PASSWORD")
            # --------------------------LIBRARIAN SECTION------------------------------
            case 2:
                lpassword="librarian22"
                l_user_password=str(input("WRITE THE PASSWORD:- "))
                if lpassword == l_user_password:
                    print("1. Librarian - Show All Users")
                    print("2. Librarian - Show Issued Books")
                    print("3. Librarian - Save Data")
                    lchoice=int(input("WHICH SERVICE YOU WANT(1-3):- "))
                    match lchoice:
                        case 1:
                            lib.show_all_users()
                        case 2:
                            lib.show_issued_books()
                        case 3:
                            lib.save_data()
                        case _:
                            print("INVALID CHOICE")
                else:
                    print("WRONG PASSWORD")
            # --------------------------------USER SECTION------------------------
            case 3:
                print("1. User - Issue Book")
                print("2. User - Return Book")
                print("3. User - View All Books")
                uchoice=int(input("WHICH SERVICE YOU WANT:- "))
                match uchoice:
                    case 1:
                        user_name = input("WRITE THE USERNAME:- ")
                        user_obj = lib.find_user_by_name(user_name)
                        book_id = int(input("ENTER THE BOOK ID:- "))
                        if user_obj:
                            lib.issue_book(book_id, user_obj)
                        else:
                            print("❌ User not found.")

                    case 2:
                        user=input("WRITE THE USERNAME:- ")
                        user_obj = lib.find_user_by_name(user)
                        if user_obj:
                            book_id = int(input("ENTER THE BOOK ID:- "))
                            lib.return_book(book_id, user_obj)
                        else:
                            print("❌ User not found.")

                    case 3:
                        lib.show_all_books()
                    case _:
                        print("INVALID CHOICE")            
            case 4:
                break
            case _:
                print("INVALID CHOICE")

main()
