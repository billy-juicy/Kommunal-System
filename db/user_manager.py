from db.db_manager import DatabaseManager

class UserManager:
    def __init__(self, db: DatabaseManager):
        self.db = db # Сохраняем подключение к бд

    # Метод для добавления пользователя в таблицу Users
    def add_user(self, фамилия, имя, отчество, телефон, адрес, email, логин, пароль, роль, client_id=None):
        query = """
        INSERT INTO Users (Фамилия, Имя, Отчество, Телефон, Адрес, Email, Логин, Пароль, Роль, client_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        self.db.execute_query(query, (фамилия, имя, отчество, телефон, адрес, email, логин, пароль, роль, client_id))

    # Метод для получения всех пользователей из таблицы Users
    def get_all_users(self):
        query = """
        SELECT user_id, Фамилия, Имя, Отчество, Телефон, Адрес, Email, Логин, Роль
        FROM Users
        ORDER BY user_id;
        """
        self.db.execute_query(query)
        return self.db.fetch_all()

    # Метод для обновления данных пользователя по user_id в таблице Users
    def update_user(self, user_id, фамилия, имя, отчество, телефон, адрес, email, логин, пароль, роль, client_id=None):
        query = """
        UPDATE Users
        SET Фамилия = %s,
            Имя = %s,
            Отчество = %s,
            Телефон = %s,
            Адрес = %s,
            Email = %s,
            Логин = %s,
            Пароль = %s,
            Роль = %s,
            client_id = %s
        WHERE user_id = %s;
        """
        self.db.execute_query(query, (фамилия, имя, отчество, телефон, адрес, email, логин, пароль, роль, client_id, user_id))

    # Метод для удаления пользователя по его user_id в таблице Users
    def delete_user(self, user_id):
        query = "DELETE FROM Users WHERE user_id = %s;"
        self.db.execute_query(query, (user_id,))