import sqlite3
import logging

NAME_BD = 'Story_Products.db'

def initiate_db():
    """Функция создаёт таблицу Products, если она ещё не создана при помощи SQL запроса."""
    try:
        logging.info((f'Попытка подключения к БД {NAME_BD}'))
        with sqlite3.connect(NAME_BD) as connection:
            logging.info((f'Подключение к БД {NAME_BD} выполнено УСЕШНО!'))
            cursor = connection.cursor()
            logging.info((f'Попытка выполнить команду создания таблицы Products'))
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL)
            ''')
            connection.commit()
            logging.info((f'Команда создания таблицы Products выполнена УСПЕШНО!'))
    except sqlite3.Error as e:
        logging.error(f'Ошибка при работе с БД: {e}')
    finally:
        logging.info(f'Подключение к БД закрыто УСПЕШНО!')


def get_all_products():
    """Функция возвращает все записи из таблицы Products, полученные при помощи SQL запроса."""
    try:
        logging.info((f'Попытка подключения к БД {NAME_BD}'))
        with sqlite3.connect(NAME_BD) as connection:
            logging.info((f'Подключение к БД {NAME_BD} выполнено УСЕШНО!'))
            cursor = connection.cursor()
            logging.info((f'Попытка выполнить команду выбрать все записи из таблицы Products'))
            cursor.execute('SELECT * FROM Products')
            rows = cursor.fetchall()
            logging.info(f'Всего получено записей из таблицы Products: {len(rows)}')
            result = []  # формируем список строк
            for row in rows:
                product = []
                product.append(row[1])      # title
                product.append(row[2])      # description
                product.append(row[3])      # price
                result.append(product)
            connection.commit()
    except sqlite3.Error as e:
        logging.error(f'Ошибка при работе с БД: {e}')
    finally:
        logging.info(f'Подключение к БД закрыто УСПЕШНО!')
        return result



def insert_multiple_lines(lines:list):
    """Функция вставляет несколько записей в таблицу"""
    try:
        logging.info((f'Попытка подключения к БД {NAME_BD}'))
        with sqlite3.connect(NAME_BD) as connection:
            logging.info((f'Подключение к БД {NAME_BD} выполнено УСЕШНО!'))
            cursor = connection.cursor()
            logging.info((f'Попытка выполнить команду вставить несколько записей в таблицу Products'))

            cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', lines)
            connection.commit()
            logging.info((f'Количество УСПЕШНО вставленных записей в таблицу Users: {cursor.rowcount}'))
    except sqlite3.Error as e:
        logging.error(f'Ошибка при работе с БД: {e}')
    finally:
        logging.info(f'Подключение к БД закрыто УСПЕШНО!')


