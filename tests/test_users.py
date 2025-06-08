import unittest
from db.db_manager import DatabaseManager
from db.user_manager import UserManager


class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager()
        self.user_manager = UserManager(self.db)

    def tearDown(self):
        self.db.close()

    def test_add_and_get_user(self):
        login = "testuseralex"

        # Очистка: если пользователь уже существует
        self.db.execute_query("DELETE FROM Users WHERE Логин = %s;", (login,))

        # Добавление пользователя
        self.user_manager.add_user(
            фамилия="Александров",
            имя="Алексей",
            отчество="Тестович",
            телефон="79522324312",
            адрес="ул. Текстовая, д. 7",
            email="test@examble.ru",
            логин=login,
            пароль="testpass",
            роль="client"
        )

        # Получаем всех пользователей и проверяем, что новый есть
        users = self.user_manager.get_all_users()
        логины = [u[7] for u in users]  # u[7] = Логин
        self.assertIn(login, логины)

    def test_delete_user(self):
        login = "testuserasugar"

        # Очистка
        self.db.execute_query("DELETE FROM Users WHERE Логин = %s;", (login,))

        # Добавление
        self.user_manager.add_user(
            фамилия="Сахаров",
            имя="Захар",
            отчество="Владимирович",
            телефон="79586321224",
            адрес="ул. Шарова, д. 21",
            email="testuser@example.com",
            логин=login,
            пароль="pass",
            роль="client"
        )

        # Получаем ID только что добавленного пользователя
        users = self.user_manager.get_all_users()
        user_id = next((u[0] for u in users if u[7] == login), None)
        self.assertIsNotNone(user_id, "User ID не найден после добавления")

        # Удаляем
        self.user_manager.delete_user(user_id)

        # Проверяем, что пользователя больше нет
        users_after = self.user_manager.get_all_users()
        ids_after = [u[0] for u in users_after]
        self.assertNotIn(user_id, ids_after)


if __name__ == '__main__':
    unittest.main()
