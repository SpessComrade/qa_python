import pytest
from main import BooksCollector

@pytest.fixture
def book1():
    collector = BooksCollector()
    collector.add_new_book('Левша')
    collector.set_book_genre('Левша', 'Детективы')
    return collector

@pytest.fixture
def two_books():
    collector = BooksCollector()
    collector.add_new_book('Правша')
    collector.set_book_genre('Правша', 'Фантастика')

    collector.add_new_book('Левша')
    collector.set_book_genre('Левша', 'Детективы')

    return collector


