import psycopg2
from config import DB_CONFIG

# Класс, в котором организуем всю работу с базой данных
class DatabaseManager:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(**DB_CONFIG) # Подключение к PostgreSQL с помощью параметров из словаря
            self.cursor = self.connection.cursor() # Сохраняем объект подключения
            print("Подключение к базе данных успешно.")

        except Exception as e:
            print("Ошибка подлючения к базе данных:", e)
            self.connection = None # Сбрасываем соединение
            self.cursor = None # Сбрасываем курсор

    # Метод, выполняющий любой SQL-запрос
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params) # params - переменные в запросе
            self.connection.commit() # Сохраняем изменения в базе

        except Exception as e:
            print("Ошибка выполнения запроса:", e)
            self.connection.rollback() # Отменяем изменения

    # Метод, использующийся после SELECT-запросов, чтобы получить все строки результата
    def fetch_all(self):
        return self.cursor.fetchall()

    # Метод, использующися для закрытия соединения и курсора, чтобы не было утечек памяти и висящих подключений
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Соединение с базой данных завершено.")