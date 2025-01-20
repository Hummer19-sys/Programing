import psycopg2

conn = psycopg2.connect(
    database="netology_db",
    user="postgres",
    password="123"
)

# Создание структуры БД
def create_db():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Clients (
        ClientID SERIAL PRIMARY KEY,
        Client_Name VARCHAR(255) NOT NULL,
        Client_Surname VARCHAR(255) NOT NULL,
        Email VARCHAR(100) NOT NULL UNIQUE);
        """)

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Phones (
        PhoneID SERIAL PRIMARY KEY,
        ClientID INT,
        Phone_Number VARCHAR(20),
        FOREIGN KEY (ClientID) REFERENCES Clients (ClientID) ON DELETE CASCADE);
        ''')
        conn.commit()
    conn.close()
pass

# Добавление нового клиента:
def adding_client(Name, Surname, Email):
    with conn.cursor() as cur:
        cur.execute('''
        INSERT INTO Clients( Client_Name, Client_Surname, Email)
        VALUES(%s, %s, %s);
        ''', (Name, Surname, Email))
        conn.commit()
    conn.close()
pass

# Добавление телефона для существующего клиента:
def adding_phone(ID, Number):
    with conn.cursor() as cur:
        cur.execute('''
        INSERT INTO Phones(ClientID, Phone_Number)
        VALUES (%s, %s);
        ''', (ID, Number))
        conn.commit()
    conn.close()
pass

# Изменение фамилии клиента:
def change_client_surname(id, surname_for_change):
    with conn.cursor() as cur:
        cur.execute(f'''
        UPDATE Clients
        SET Client_Surname = %s
        WHERE ClientID= %s;
        ''', (surname_for_change, id))
        conn.commit()
    conn.close()
pass

# Изменение имени клиента:
def change_client_name(id, name_for_change):
    with conn.cursor() as cur:
        cur.execute('''
        UPDATE Clients
        SET Client_Name = %s
        WHERE ClientID= %s;
        ''', (name_for_change, id))
        conn.commit()
    conn.close()
pass

# Изменение email клиента:
def change_client_email(id, email_for_change):
    with conn.cursor() as cur:
        cur.execute('''
        UPDATE Clients
        SET Email = %s
        WHERE ClientID= %s;
        ''', (email_for_change, id))
        conn.commit()
    conn.close()
pass

# Удаление телефона для клиента:
def delete_phone(id):
    with conn.cursor() as cur:
        cur.execute('''
        DELETE FROM Phones
        WHERE ClientID = %s;
        ''', (id,))
        conn.commit()
    conn.close()
pass

# Удаление клиента:
def delete_client(id):
    with conn.cursor() as cur:
        cur.execute('''
        DELETE FROM Clients
        WHERE ClientID = %s;
        ''', (id,))
        conn.commit()
    conn.close()
pass

# поиск клиента по его данным:
def find_client(name=None, surname=None, email=None, phone=None):
    with conn.cursor() as cur:
        query = '''
        SELECT * FROM Clients
        JOIN Phones ON Clients.ClientID = Phones.ClientID
        '''

        params = []
        conditions = []

        if name:
            conditions.append('Client_Name = %s')
            params.append(name)
        if surname:
            conditions.append('Client_Surname = %s')
            params.append(surname)
        if email:
            conditions.append('Email = %s')
            params.append(email)
        if phone:
            conditions.append('Phone_Number = %s')
            params.append(phone)

        if conditions:
            query += ' WHERE ' + ' AND '.join(conditions)

        cur.execute(query, params)
        results = cur.fetchall()

        for row in results:
            print(row)

        return results

    conn.close()
pass

# create_db()
# adding_client('Ivan', 'Ivanov', 'ivan.ivanov@mail.ru')
# adding_phone(1, 81234567890)
# change_client_surname(1, 'Petrov')
# change_client_name(1, 'Petr')
# change_client_email(1, 'petr.petrov@mail.ru')
# find_client(name='Petr')
# delete_phone(1)
# delete_client(1)
