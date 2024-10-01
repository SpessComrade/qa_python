import pytest

from main import BooksCollector


class TestBooksCollector:


    # Добавление новой книги. Жанр не должен быть указан.
    def test_add_new_book_title_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мёртвые души')
        assert 'Мёртвые души' in collector.books_genre
        assert collector.books_genre['Мёртвые души'] == ''

    # Проверка, что книга с названием больше 40 символов не добавляется
    def test_add_new_book_title_length_exceeded_book_not_added(self):
        collector = BooksCollector()
        title = '9' * 41
        collector.add_new_book(title)
        assert title not in collector.books_genre

    # Проверка, что книга с пустым названием не добавляется
    def test_add_new_book_empty_title_book_not_added(self):
        collector = BooksCollector()
        title = ''
        collector.add_new_book(title)
        assert title not in collector.books_genre

    # Проверка, что не добавляется вторая книга с одинаковым названием
    def test_add_new_book_same_title_one_book_added(self):
        collector = BooksCollector()
        title = 'Левша'
        collector.add_new_book(title)
        collector.add_new_book(title)
        assert len(collector.books_genre) == 1

    #Проверка присвоения жанра книги. Не стал пользоваться фикстурой, чтобы вызвать метод в тесте.
    def test_set_book_genre_book_title_book_genre_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Левша')
        collector.set_book_genre('Левша', 'Детективы')

        assert collector.books_genre['Левша'] == 'Детективы'


    #Проверка, что книге не присваивается некорректный жанр
    @pytest.mark.parametrize('genre', ['Дефективы', '34252f', 123, None])
    def test_set_book_genre_invalid_genre_genre_not_set(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Левша')
        collector.set_book_genre('Левша', genre)

        assert collector.books_genre['Левша'] == ''


    #Проверка, получения жанра книги
    def test_get_book_genre_title_genre_return_genre(self, book1):
        genre = book1.get_book_genre('Левша')

        assert genre == 'Детективы'

    #Проверка получения корректной книги по жанру. В фикстуре создаются 2 книги разных жанров.
    def test_get_books_with_specific_genre_title_genre_book(self, two_books):
        books = two_books.get_books_with_specific_genre('Детективы')

        assert books == ['Левша']

    #Проверка получения корректного списка жанров
    def test_get_books_genre_genres_dictionary(self):
        collector = BooksCollector()
        genres_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

        assert genres_list == collector.genre

    #Проверяем, что из двух книг жанров Детективы и Фантастика добавилась только книга жанра Фантастика
    def test_get_books_for_children_two_books_one_child_book(self, two_books):
        books = two_books.get_books_for_children()

        assert books == ['Правша']


    #Проверка добавления существующей книги в избранное
    def test_add_book_in_favorites_one_book_added_to_favorites(self, book1):
        collector = book1
        collector.add_book_in_favorites('Левша')
        assert 'Левша' in book1.favorites


    #Проверка, что несуществующая книга не добавлена в избранное
    def test_add_book_in_favorites_nonexisting_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Левша')
        assert 'Левша' not in collector.favorites

    #Проверка, что из двух одинаковых книг в избранное добавится только одна
    def test_add_book_in_favorites_already_existing_book_not_added(self, book1):
        collector = book1
        collector.add_book_in_favorites('Левша')
        collector.add_book_in_favorites('Левша')

        assert len(collector.favorites) == 1


    #Проверка удаления добавленной книги из избранного
    def test_delete_book_from_favorites_existing_book_book_removed(self, book1):
        collector = book1
        collector.add_book_in_favorites('Левша')
        collector.delete_book_from_favorites('Левша')

        assert 'Левша' not in collector.favorites


    #Проверка отсутствия удаления не указанных книг из избранного
    def test_delete_book_from_favorites_multiple_existing_books_one_book_removed(self, two_books):
        collector = two_books
        collector.add_book_in_favorites('Левша')
        collector.add_book_in_favorites('Правша')
        collector.delete_book_from_favorites('Левша')

        assert 'Правша' in collector.favorites and 'Левша' not in collector.favorites


    #Проверка отображения списка Избранного
    def test_get_list_of_favorites_books_favorited_books_list_of_books(self, two_books):
        collector = two_books
        collector.add_book_in_favorites('Левша')
        collector.add_book_in_favorites('Правша')

        assert collector.get_list_of_favorites_books() == ['Левша', 'Правша']
