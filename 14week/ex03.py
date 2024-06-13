# 책 클래스
class Book:
    def __init__(self, title, author, isbn, is_borrowed):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = is_borrowed

    # 책 대출
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'{self.title}이 대출되었습니다.')
        else:
            print(f'{self.title}은 대출 중입니다.')

    # 책 반납
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'{self.title}이 반납되었습니다.')
        else:
            print(f'{self.title}은 대출 중이 아닙니다.')

    # 책 정보 출력


my_book_1 = Book('1084', '무라카이 하무리', 182673623, False)


class Library:
    # 도서관 이름, 회원 목록, 책 목록
    def __init__(self, title):
        self.title = title
        self.members = []
        self.books = []

    # 멤버 추가
    def add_member(self, member):
        if member not in self.members:
            self.members.append(member)
            print(f'{member.name}이 등록되었습니다.')
        else:
            print(f'{member.name}은 등록된 회원입니다.')

    # 멤버 제거
    def del_member(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f'{member.name}이 탈퇴되었습니다.')
        else:
            print(f'{member.name}은 등록되지 않은 회원입니다.')

    # 책 주가
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f'{book.title}이 등록되었습니다.')
        else:
            print(f'{book.title}은 등록된 책입니다..')

    # 책 추가
    def del_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'{book.title}이 반출되었습니다.')
        else:
            print(f'{book.title}은 등록되지 않은 책입니다..')

    # 정보 출력
    def __str__(self):
        members_info = [m.name for m in self.members]
        books_info = [b.title for b in self.books]
        return f'도서관 이름 : {self.title} /멤버 : {members_info} / 책 : {books_info}'


library = Library('동아대')