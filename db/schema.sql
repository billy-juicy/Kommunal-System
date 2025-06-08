-- Таблица: Clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,
    Фамилия VARCHAR(50),
    Имя VARCHAR(50),
    Отчество VARCHAR(50),
    Телефон VARCHAR(20),
    Адрес VARCHAR(255),
    Email VARCHAR(100)
);

-- Создаем явный тип
CREATE TYPE user_role AS ENUM ('client', 'admin');

-- Таблица: Users
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    Фамилия VARCHAR(50),
    Имя VARCHAR(50),
    Отчество VARCHAR(50),
    Телефон VARCHAR(20),
    Адрес VARCHAR(255),
    Email VARCHAR(100),
    Логин VARCHAR(50) UNIQUE NOT NULL,
    Пароль VARCHAR(255) NOT NULL,
    Дата_регистрации DATE DEFAULT CURRENT_DATE,
    Роль user_role NOT NULL,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

-- Таблица: Properties
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    Собственник VARCHAR(100),
    Адрес VARCHAR(255),
    Тип VARCHAR(50),
    Площадь NUMERIC(10,2),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

-- Таблица: Complaints
CREATE TABLE Complaints (
    complaint_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    Описание_жалобы TEXT,
    Статус_жалобы VARCHAR(50),
    Дата_создания DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
);

-- Таблица: Services
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY,
    Название VARCHAR(100),
    Единица_измерения VARCHAR(50)
);

-- Таблица: Tariffs
CREATE TABLE Tariffs (
    tariff_id SERIAL PRIMARY KEY,
    service_id INT NOT NULL,
    Тариф NUMERIC(10,2),
    Дата_начала DATE,
    Дата_окончания DATE,
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Таблица: Invoices
CREATE TABLE Invoices (
    invoice_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    Общая_сумма_к_оплате NUMERIC(10,2),
    Дата_формирования_квитанции DATE,
    Срок_оплаты DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Таблица: Debts
CREATE TABLE Debts (
    debt_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    Сумма_задолженности NUMERIC(10,2),
    Срок_погашения DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Таблица: Payments
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    Сумма_платежа NUMERIC(10,2),
    Дата_платежа DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Таблица: Meters
CREATE TABLE Meters (
    meter_id SERIAL PRIMARY KEY,
    client_id INT NOT NULL,
    service_id INT NOT NULL,
    Номер_счётчика VARCHAR(100),
    Дата_установки DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
);

-- Таблица: MeterReadings
CREATE TABLE MeterReadings (
    reading_id SERIAL PRIMARY KEY,
    meter_id INT NOT NULL,
    Показание_счётчика NUMERIC(10,2),
    Дата_подачи_показания DATE,
    FOREIGN KEY (meter_id) REFERENCES Meters(meter_id)
);
