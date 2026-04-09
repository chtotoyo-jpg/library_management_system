"""
Главный модуль запуска приложения Library Management System.
Точка входа в программу.
"""

import sys
from book_manager import add_book, find_book, get_all_books, remove_book


def display_menu() -> str:
    """Отображает главное меню консольного приложения."""
    print("\n" + "=" * 40)
    print("   БИБЛИОТЕЧНАЯ СИСТЕМА УПРАВЛЕНИЯ   ")
    print("=" * 40)
    print("1. Добавить книгу")
    print("2. Найти книгу")
    print("3. Показать все книги")
    print("4. Удалить книгу")
    print("5. Выйти")
    print("-" * 40)
    return input("Выберите опцию (1-5): ").strip()


def handle_add_book() -> None:
    """Обработчик добавления новой книги."""
    title = input("Введите название книги: ")
    add_book(title)


def handle_find_book() -> None:
    """Обработчик поиска книги."""
    title = input("Введите название книги для поиска: ")
    if find_book(title):
        print(f"Книга '{title}' найдена в каталоге.")
    else:
        print(f"Книга '{title}' не найдена.")


def handle_list_books() -> None:
    """Обработчик отображения всех книг."""
    books = get_all_books()
    if books:
        print("\nСписок книг в каталоге:")
        for i, book in enumerate(books, 1):
            print(f"  {i}. {book}")
        print(f"Всего книг: {len(books)}")
    else:
        print("Каталог пуст. Добавьте книги через опцию 1.")


def handle_remove_book() -> None:
    """Обработчик удаления книги."""
    title = input("Введите название книги для удаления: ")
    remove_book(title)


def main() -> None:
    """Основной цикл программы."""
    print("\nСистема управления библиотекой успешно инициализирована.")
    print("Версия: 1.0.0")
    
    # Словарь для сопоставления выбора пользователя с функциями-обработчиками
    menu_actions = {
        "1": handle_add_book,
        "2": handle_find_book,
        "3": handle_list_books,
        "4": handle_remove_book,
    }
    
    while True:
        choice = display_menu()
        
        if choice == "5":
            print("\nЗавершение работы программы. До свидания!")
            sys.exit(0)
        elif choice in menu_actions:
            try:
                menu_actions[choice]()
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 5.")


if __name__ == "__main__":
    main()