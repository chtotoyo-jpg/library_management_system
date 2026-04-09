"""
Модульные тесты для модуля book_manager.py.
Проверяют корректность работы функций после исправлений (post-review).
"""

import unittest
import sys
import os

# Добавляем путь к src, чтобы импорт работал корректно
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import book_manager


class TestBookManager(unittest.TestCase):
    """Набор тестов для проверки корректности работы с каталогом."""
    
    def setUp(self) -> None:
        """Выполняется перед каждым тестом. Очищает каталог."""
        book_manager.library_catalog.clear()
        # Добавляем тестовые данные для некоторых тестов
        book_manager.library_catalog.extend(["Война и мир", "Преступление и наказание"])
    
    def test_add_book_valid_string(self) -> None:
        """Проверка успешного добавления валидной строки."""
        result = book_manager.add_book("Мастер и Маргарита")
        self.assertTrue(result)
        self.assertIn("Мастер и Маргарита", book_manager.get_all_books())
    
    def test_add_book_strips_whitespace(self) -> None:
        """Проверка, что функция обрезает пробелы по краям."""
        result = book_manager.add_book("   Анна Каренина   ")
        self.assertTrue(result)
        self.assertIn("Анна Каренина", book_manager.get_all_books())
        self.assertNotIn("   Анна Каренина   ", book_manager.get_all_books())
    
    def test_add_book_empty_string_returns_false(self) -> None:
        """Проверка, что пустая строка НЕ добавляется и возвращает False."""
        initial_count = len(book_manager.get_all_books())
        result = book_manager.add_book("")
        self.assertFalse(result)
        self.assertEqual(len(book_manager.get_all_books()), initial_count)
    
    def test_add_book_whitespace_only_returns_false(self) -> None:
        """Проверка, что строка из пробелов НЕ добавляется."""
        initial_count = len(book_manager.get_all_books())
        result = book_manager.add_book("     ")
        self.assertFalse(result)
        self.assertEqual(len(book_manager.get_all_books()), initial_count)
    
    def test_add_book_invalid_type_returns_false(self) -> None:
        """Проверка, что передача числа вместо строки возвращает False."""
        result = book_manager.add_book(12345)
        self.assertFalse(result)
        result = book_manager.add_book(None)
        self.assertFalse(result)
        result = book_manager.add_book(["список", "вместо", "строки"])
        self.assertFalse(result)
    
    def test_find_existing_book(self) -> None:
        """Поиск существующей книги."""
        self.assertTrue(book_manager.find_book("Война и мир"))
    
    def test_find_book_case_sensitive(self) -> None:
        """Поиск регистрозависимый (особенность реализации)."""
        self.assertFalse(book_manager.find_book("война и мир"))  # строчные буквы
    
    def test_find_book_with_whitespace(self) -> None:
        """Поиск книги с пробелами в запросе."""
        self.assertTrue(book_manager.find_book("  Война и мир  "))
    
    def test_find_non_existing_book(self) -> None:
        """Поиск отсутствующей книги."""
        self.assertFalse(book_manager.find_book("Несуществующая книга"))
    
    def test_remove_existing_book(self) -> None:
        """Удаление существующей книги."""
        initial_count = len(book_manager.get_all_books())
        result = book_manager.remove_book("Война и мир")
        self.assertTrue(result)
        self.assertEqual(len(book_manager.get_all_books()), initial_count - 1)
        self.assertNotIn("Война и мир", book_manager.get_all_books())
    
    def test_remove_non_existing_book(self) -> None:
        """Удаление несуществующей книги."""
        initial_count = len(book_manager.get_all_books())
        result = book_manager.remove_book("Невидимый мир")
        self.assertFalse(result)
        self.assertEqual(len(book_manager.get_all_books()), initial_count)
    
    def test_get_all_books_returns_copy(self) -> None:
        """Проверка, что get_all_books возвращает копию, а не ссылку."""
        books_copy = book_manager.get_all_books()
        books_copy.append("Новая книга")
        self.assertNotIn("Новая книга", book_manager.library_catalog)


if __name__ == '__main__':
    unittest.main()