import sqlite3
import random


class withDataBase:
    def make_new_database(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE users
                  (id text, nickname text, admincode text)
               """)
        cursor.execute("""CREATE TABLE admins
                  (id text, nickname text, admincode text)
               """)
        conn.close()
    def takeFromBase(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        new_datas = cursor.fetchall()
        return new_datas
        conn.close()
    def takeFromBase_admin(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM admins"
        cursor.execute(sql)
        new_datas = cursor.fetchall()
        return new_datas
        conn.close()
    def addToBase(self, data_id, data_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users WHERE id = ?", (data_id,))
        data=cursor.fetchone()[0]
        if data == 0:
            cursor.execute('''INSERT INTO users(id, nickname) VALUES (?, ?)''', (data_id, data_name))
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False
    def addToBase_admin(self, data_id, data_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM admins WHERE id = ?", (data_id,))
        data=cursor.fetchone()[0]
        if data == 0:
            cursor.execute('''INSERT INTO admins(id, nickname) VALUES (?, ?)''', (data_id, data_name))
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    def update_base(self, data_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET access = 'end' WHERE id = ?", (data_id,))
        conn.commit()

    def make_admin_code(self):
        randome_8 = str(random.randint(10000000, 99999999))
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO admins(id, nickname, admincode) VALUES (?, ?, ?)''', ('', '', str(randome_8)))
        conn.commit()
        conn.close()


    def addToBaseAdmins(self, data_id, data_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO users(id, nickname) VALUES (?, ?)''', (data_id, data_name))
        conn.commit()
        conn.close()

    def deleteFromBase(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "DELETE FROM users WHERE id = '1234134'"
        cursor.execute(sql)
        conn.commit()
        conn.close()

    def test(self, data_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM users WHERE id = ?", (data_id,))
        data=cursor.fetchone()[0]
        if data == 0:
            print("Нет пользователя")
        else:
            print("Пользователь есть")
        '''sql = "SELECT * FROM users WHERE id LIKE '12345'"
        cursor.execute(sql)
        new_datas = cursor.fetchall()
        print(new_datas[0][0])

        sql = """SELECT id FROM users WHERE id=?"""
        cursor.execute(sql, [(data_id)])
        if cursor.fetchone()[0] != str(data_id): print('Нет таких пользователей')
        else: print('Есть пользователь')'''
        '''sql = "SELECT access FROM users WHERE name LIKE 'prostohel'"
        cursor.execute(sql)
        new_datas = cursor.fetchall()'''
        conn.close()
workWithBase = withDataBase()
