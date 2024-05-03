from dataclasses import dataclass
from typing import List, Sequence


@dataclass
class Book:
    title: str
    author: str
    genre: str
    num_pages: int
    publication_year: int


book_t = List[str, str, str, int, int]


def add_book(books_list: List[Book], new_book_args: book_t) -> List[Book]:
    new_book = Book(*new_book_args)
    books_list.append(new_book)
    return books_list


def find_by_author(books_list: List[Book], author: str) -> List[Book]:
    found_books = []
    for book in books_list:
        if book.author == author:
            found_books.append(book)
    return found_books


def find_longest_book(books_list: List[Book]):
    return max([book.num_pages for book in books_list])


def count_books(books_list: List[Book]):
    return len(books_list)
